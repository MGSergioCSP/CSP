import pymysql
import os
from datetime import datetime
from modelos import Ingrediente, LinaIngrediente, Plato, EntradaMenu

class RecetasMariaDBDAO:
    def __init__(self, host='localhost', user='root', password='', db='recetas_db'):
        self.config = {
            'host': host,
            'user': user,
            'password': password
        }
        self.db_name = db
        self._crear_base_de_datos()
        self.config['database'] = self.db_name
        self._crear_taboas()

    def _conectar(self):
        return pymysql.connect(**self.config)

    def _crear_base_de_datos(self):
        conn = pymysql.connect(host=self.config['host'], user=self.config['user'], password=self.config['password'])
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.db_name}")
        conn.commit()
        conn.close()

    def _crear_taboas(self):
        with self._conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS ingredientes (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nome VARCHAR(255) NOT NULL UNIQUE
                    )
                ''')
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS platos (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nome VARCHAR(255) NOT NULL,
                        tempada VARCHAR(100),
                        preparacion TEXT,
                        fotoUrl VARCHAR(255)
                    )
                ''')
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS lina_ingredientes (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        plato_id INT,
                        ingrediente_id INT,
                        cantidade FLOAT,
                        unidade VARCHAR(50),
                        FOREIGN KEY (plato_id) REFERENCES platos (id) ON DELETE CASCADE,
                        FOREIGN KEY (ingrediente_id) REFERENCES ingredientes (id)
                    )
                ''')
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS entrada_menus (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        plato_id INT,
                        datafecha DATE,
                        momento VARCHAR(100),
                        FOREIGN KEY (plato_id) REFERENCES platos (id) ON DELETE CASCADE
                    )
                ''')
            conn.commit()

    def gardar_ingrediente(self, ingrediente: Ingrediente):
        with self._conectar() as conn:
            self._gardar_ingrediente_conn(conn, ingrediente)
            conn.commit()

    def _gardar_ingrediente_conn(self, conn, ingrediente):
        with conn.cursor() as cursor:
            try:
                cursor.execute("INSERT INTO ingredientes (nome) VALUES (%s)", (ingrediente.get_nome(),))
                ingrediente.id = cursor.lastrowid
            except pymysql.err.IntegrityError:
                # Xa existe
                cursor.execute("SELECT id FROM ingredientes WHERE nome = %s", (ingrediente.get_nome(),))
                res = cursor.fetchone()
                if res:
                    ingrediente.id = res[0]

    def obter_ingrediente(self, id: int) -> Ingrediente:
        with self._conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, nome FROM ingredientes WHERE id = %s", (id,))
                row = cursor.fetchone()
                if row:
                    ing = Ingrediente(row[1])
                    ing.id = row[0]
                    return ing
        return None

    def gardar_plato(self, plato: Plato):
        with self._conectar() as conn:
            self._gardar_plato_conn(conn, plato)
            conn.commit()

    def _gardar_plato_conn(self, conn, plato: Plato):
        with conn.cursor() as cursor:
            cursor.execute('''
                INSERT INTO platos (nome, tempada, preparacion, fotoUrl)
                VALUES (%s, %s, %s, %s)
            ''', (plato._nome, plato._tempada, plato._preparacion, plato._fotoUrl))
            plato.id = cursor.lastrowid
            
            for lina in plato._ingredientes:
                if not lina._ingrediente.id:
                    self._gardar_ingrediente_conn(conn, lina._ingrediente)
                
                cursor.execute('''
                    INSERT INTO lina_ingredientes (plato_id, ingrediente_id, cantidade, unidade)
                    VALUES (%s, %s, %s, %s)
                ''', (plato.id, lina._ingrediente.id, lina._cantidade, lina._unidade))
                lina.id = cursor.lastrowid

    def obter_plato(self, id: int) -> Plato:
        with self._conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, nome, tempada, preparacion, fotoUrl FROM platos WHERE id = %s", (id,))
                row = cursor.fetchone()
                if not row:
                    return None
                
                plato = Plato(row[1], row[2], row[3], row[4])
                plato.id = row[0]
                
                cursor.execute('''
                    SELECT l.id, l.cantidade, l.unidade, i.id, i.nome 
                    FROM lina_ingredientes l
                    JOIN ingredientes i ON l.ingrediente_id = i.id
                    WHERE l.plato_id = %s
                ''', (plato.id,))
                
                for l_row in cursor.fetchall():
                    ing = Ingrediente(l_row[4])
                    ing.id = l_row[3]
                    lina = LinaIngrediente(l_row[1], l_row[2], ing)
                    lina.id = l_row[0]
                    plato.engadirIngrediente(lina)
                return plato

    def gardar_entrada_menu(self, entrada: EntradaMenu):
        with self._conectar() as conn:
            if not entrada._plato.id:
                self._gardar_plato_conn(conn, entrada._plato)
            
            with conn.cursor() as cursor:
                cursor.execute('''
                    INSERT INTO entrada_menus (plato_id, datafecha, momento)
                    VALUES (%s, %s, %s)
                ''', (entrada._plato.id, entrada._data.isoformat(), entrada._momento))
                entrada.id = cursor.lastrowid
            conn.commit()

    def obter_todas_entradas(self) -> list:
        entradas = []
        with self._conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, plato_id, datafecha, momento FROM entrada_menus")
                rows = cursor.fetchall()
                for r in rows:
                    plato = self.obter_plato(r[1])
                    # pymysql DATE field comes as datetime.date usually, but let's be safe
                    data = r[2] if hasattr(r[2], 'year') else datetime.fromisoformat(str(r[2])).date()
                    entrada = EntradaMenu(data, r[3], plato)
                    entrada.id = r[0]
                    entradas.append(entrada)
        return entradas
