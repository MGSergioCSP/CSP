def mostrar_menu():
    print("\n=== CRIPTO WALLET V1.0 ===")
    print("1. Registrar nueva inversión")
    print("2. Ver activos (resumen)")
    print("3. Ver balance total (USD/Euro)")
    print("4. Salir")

def pedir_transaccion() -> dict:
    """Pide datos al usuario y valida tipos básicos."""
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
    print("\n=== ACTIVOS ===")
    # Uso de items() para iterar diccionario
    for moneda, cantidad in resumen.items():
        print(f"{moneda:<5}: {cantidad:>10.4f}")