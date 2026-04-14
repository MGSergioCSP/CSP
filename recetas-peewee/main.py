from datetime import date
from modelos import Ingrediente, LinaIngrediente, Plato, EntradaMenu, XestorMenu, inicializar_db

def main():
    print("Inicializando base de datos local SQLite con Peewee...")
    inicializar_db()

    # Creando os ingredientes a través de factory method
    sardina = Ingrediente.crear_dende_string("Sardiña")
    pan = Ingrediente.crear_dende_string("Pan de Millo")

    # Crear plato (usando ORM active record)
    plato = Plato.create(
        nome="Sardiñas asadas con pan ORM",
        tempada="Verán",
        preparacion="Asar as sardiñas na brasa.",
        fotoUrl="url_da_foto"
    )

    print(f"Gardouse o plato no ORM. Engadindo ingredientes...")
    
    lina1 = LinaIngrediente.create(
        plato=plato,
        ingrediente=sardina,
        cantidade=4,
        unidade="unidade"
    )
    
    lina2 = LinaIngrediente.create(
        plato=plato,
        ingrediente=pan,
        cantidade=200,
        unidade="g"
    )

    # Menú Xestión
    hoxe = date.today()
    entrada = EntradaMenu(data=hoxe, momento="Xantar", plato=plato)
    
    xestor = XestorMenu()
    xestor.xestionar(entrada) # Isto xa fai o .save() en base de datos internamente no noso modelo

    print("\n--- Lectura dende a BD ---")
    xestor_novo = XestorMenu()
    xestor_novo.cargar_dende_base()
    
    print(xestor_novo)
    
    # Amosar plato
    plato_recuperado = Plato.get_by_id(plato.id)
    print(f"\nDatos do plato recuperado (ID {plato.id}):")
    print(plato_recuperado)

if __name__ == "__main__":
    main()
