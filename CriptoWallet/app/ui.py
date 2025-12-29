"""
Módulo de interfaz de usuario por consola.

Define las funciones necesarias para interactuar con el usuario, mostrar menús
y capturar datos de transacciones de forma segura y validada.
"""

def mostrar_menu():
    """Muestra el menú principal de la aplicación en la consola."""
    print("\n=== CRIPTO WALLET V1.0 ===")
    print("1. Registrar nueva inversión")
    print("2. Ver activos (resumen)")
    print("3. Ver balance total (USD/Euro)")
    print("4. Salir")

def pedir_transaccion() -> dict:
    """
    Solicita al usuario los datos de una nueva transacción.

    Realiza validaciones para asegurar que el símbolo de la moneda sea una cadena
    y que la cantidad ingresada sea un número positivo.

    Returns:
        dict: Un diccionario con las claves 'moneda' y 'cantidad'.
    """
    moneda = input("Introduce el símbolo (BTC, ETH...): ").upper()
    while True:
        try:
            cantidad = float(input(f"¿Qué cantidad de {moneda} has comprado?: "))
            if cantidad > 0:
                break
            print("La cantidad debe ser positiva.")
        except ValueError:
            print("Por favor, introduce un número válido.")
            
    return {"moneda": moneda, "cantidad": cantidad}

def mostrar_activos(resumen: dict):
    """
    Imprime en pantalla un resumen de los activos actuales.

    Args:
        resumen (dict): Un diccionario donde las claves son las monedas y
                        los valores son las cantidades acumuladas.
    """
    print("\n=== ACTIVOS ===")
    # Uso de items() para iterar diccionario
    for moneda, cantidad in resumen.items():
        print(f"{moneda:<5}: {cantidad:>10.4f}")