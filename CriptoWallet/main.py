"""
Módulo principal del proyecto CriptoWallet.

Este módulo coordina la ejecución del programa, gestionando el flujo entre
la interfaz de usuario, la lógica de negocio y la persistencia de datos.
"""

from app import data_manager, crypto_logic, ui          # Están en un subdirectorio app/

def main():
    """
    Punto de entrada principal de la aplicación.
    
    Carga los datos iniciales y gestiona el bucle principal del menú interactivo.
    """
    # 1. Carga del estado inicial
    cartera = data_manager.cargar_datos()

    while True:
        ui.mostrar_menu()
        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                # Registrar
                nueva_tx = ui.pedir_transaccion()
                cartera.append(nueva_tx)
                data_manager.guardar_datos(cartera)
                print("Inversión registrada.")
            
            case "2":
                # Ver resumen por monedas
                resumen = crypto_logic.calcular_totales(cartera)
                ui.mostrar_activos(resumen)
            
            case "3":
                # Ver valor total
                total = crypto_logic.calcular_balance_usd(cartera)
                print(f"\n VALOR TOTAL DEL PORTAFOLIO: ${total:,.2f} USD/Euro")
            
            case "4":
                print("¡Hasta luego!")
                break
            
            case _:
                print("Opción no válida.")

if __name__ == "__main__":
    main()