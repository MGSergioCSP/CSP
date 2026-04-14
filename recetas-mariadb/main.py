from datetime import date
from modelos import Ingrediente, LinaIngrediente, Plato, EntradaMenu, XestorMenu
from db_mariadb import RecetasMariaDBDAO

def main():
    print("Inicializando DAO de MariaDB...")
    # Asegúrate de ter MariaDB correndo con root e sen contrasinal (ou axusta os parámetros)
    dao = RecetasMariaDBDAO(user='root', password='')

    # Crear algúns ingredientes
    sardina = Ingrediente("Sardiña")
    pan = Ingrediente("Pan de Millo")

    # Crear un plato con liñas
    plato = Plato("Sardiñas asadas con pan", "Verán", "Asar as sardiñas na brasa.", "url_da_foto")
    plato.engadirIngrediente(LinaIngrediente(4, "unidade", sardina))
    plato.engadirIngrediente(LinaIngrediente(200, "g", pan))

    print(f"Gardando {plato.get_nome()} na base de datos...")
    dao.gardar_plato(plato)
    
    # Crear e gardar unha entrada de menú
    hoxe = date.today()
    entrada = EntradaMenu(hoxe, "Xantar", plato)
    
    print("Gardando entrada do menú na base de datos...")
    dao.gardar_entrada_menu(entrada)

    # Obter os datos para verificar
    print("\n--- Recuperando da Base de Datos ---")
    xestor = XestorMenu()
    entradas_gardadas = dao.obter_todas_entradas()
    for e in entradas_gardadas:
        xestor.xestionar(e)

    print(xestor)

    # Amosar os ingredientes
    plato_recuperado = dao.obter_plato(plato.id)
    print(f"\nDatos do plato recuperado (ID {plato.id}):")
    print(plato_recuperado)

if __name__ == "__main__":
    main()
