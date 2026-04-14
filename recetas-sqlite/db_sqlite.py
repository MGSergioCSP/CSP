import sqlite3
from datetime import datetime
from modelos import Ingrediente, LinaIngrediente, Plato, EntradaMenu

class RecetasDAO:
    def __init__(self, db_path="recetas.db"):
        self.db_path = db_path
        self._crear_taboas()

    def _conectar(self):
        return sqlite3.connect(self.db_path)

    def _crear_taboas(self):
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS ingredientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL UNIQUE
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS platos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    tempada TEXT,
                    preparacion TEXT,
                    fotoUrl TEXT
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS lina_ingredientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    plato_id INTEGER,
                    ingrediente_id INTEGER,
                    cantidade REAL,
                    unidade TEXT,
                    FOREIGN KEY (plato_id) REFERENCES platos (id),
                    FOREIGN KEY (ingrediente_id) REFERENCES ingredientes (id)
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS entrada_menus (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    plato_id INTEGER,
                    datafecha TEXT,
                    momento TEXT,
                    FOREIGN KEY (plato_id) REFERENCES platos (id)
                )
            ''')
            conn.commit()

    def gardar_ingrediente(self, ingrediente: Ingrediente):
        with self._conectar() as conn:
            self._gardar_ingrediente_conn(conn, ingrediente)
            conn.commit()

    def _gardar_ingrediente_conn(self, conn, ingrediente):
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO ingredientes (nome) VALUES (?)", (ingrediente.get_nome(),))
            ingrediente.id = cursor.lastrowid
        except sqlite3.IntegrityError:
            # Xa existe, procedemos a buscalo para asignarlle o id
            cursor.execute("SELECT id FROM ingredientes WHERE nome = ?", (ingrediente.get_nome(),))
            res = cursor.fetchone()
            if res:
                ingrediente.id = res[0]

    def obter_ingrediente(self, id: int) -> Ingrediente:
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome FROM ingredientes WHERE id = ?", (id,))
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
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO platos (nome, tempada, preparacion, fotoUrl)
            VALUES (?, ?, ?, ?)
        ''', (plato._nome, plato._tempada, plato._preparacion, plato._fotoUrl))
        plato.id = cursor.lastrowid
        
        for lina in plato._ingredientes:
            # Asegurarse de que o ingrediente está gardado
            if not lina._ingrediente.id:
                self._gardar_ingrediente_conn(conn, lina._ingrediente)
            
            cursor.execute('''
                INSERT INTO lina_ingredientes (plato_id, ingrediente_id, cantidade, unidade)
                VALUES (?, ?, ?, ?)
            ''', (plato.id, lina._ingrediente.id, lina._cantidade, lina._unidade))
            lina.id = cursor.lastrowid

    def obter_plato(self, id: int) -> Plato:
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, tempada, preparacion, fotoUrl FROM platos WHERE id = ?", (id,))
            row = cursor.fetchone()
            if not row:
                return None
            
            plato = Plato(row[1], row[2], row[3], row[4])
            plato.id = row[0]
            
            # Cargar liñas de ingrediente
            cursor.execute('''
                SELECT l.id, l.cantidade, l.unidade, i.id, i.nome 
                FROM lina_ingredientes l
                JOIN ingredientes i ON l.ingrediente_id = i.id
                WHERE l.plato_id = ?
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
            
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO entrada_menus (plato_id, datafecha, momento)
                VALUES (?, ?, ?)
            ''', (entrada._plato.id, entrada._data.isoformat(), entrada._momento))
            entrada.id = cursor.lastrowid
            conn.commit()

    def obter_todas_entradas(self) -> list:
        entradas = []
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, plato_id, datafecha, momento FROM entrada_menus")
            rows = cursor.fetchall()
            for r in rows:
                plato = self.obter_plato(r[1])
                data = datetime.fromisoformat(r[2]).date()
                entrada = EntradaMenu(data, r[3], plato)
                entrada.id = r[0]
                entradas.append(entrada)
        return entradas
