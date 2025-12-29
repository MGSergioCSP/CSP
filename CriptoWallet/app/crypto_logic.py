"""
Módulo de lógica de negocio para el cálculo de activos criptográficos.

Proporciona funciones para obtener cotizaciones simuladas y realizar cálculos
sobre el balance y los totales del portafolio.
"""

# Diccionario simulado de precios actuales (en un caso real, usaríamos una API que acceda a datos en tiempo real)
# Ejemplos de APIs: CoinGecko, CoinMarketCap, etc.
COTIZACIONES = {
    "BTC": 65000.0, # Precio simulado de Bitcoin en USD
    "ETH": 3500.0,  # Precio simulado de Ethereum en USD
    "SOL": 140.0,   # Precio simulado de Solana en USD
    "USDT": 1.0     # Precio simulado de Tether en USD
}

def obtener_valor_actual(moneda: str) -> float:
    """
    Devuelve el valor actual de una moneda en USD.

    Args:
        moneda (str): El símbolo de la moneda (ej. 'BTC').

    Returns:
        float: El precio actual de la moneda o 0.0 si no se encuentra en las cotizaciones.
    """
    return COTIZACIONES.get(moneda.upper(), 0.0) # Se utiliza get para evitar KeyError en el diccionario

def calcular_totales(transacciones: list) -> dict:
    """
    Calcula el total acumulado por cada tipo de moneda en el portafolio.

    Args:
        transacciones (list): Una lista de diccionarios, donde cada diccionario
                              contiene 'moneda' y 'cantidad'.

    Returns:
        dict: Un diccionario con las monedas como claves y sus cantidades totales como valores.
    """
    totales = {}
    for t in transacciones:         # Lista de diccionarios
        moneda = t['moneda']
        cantidad = t['cantidad']
        
        # Uso de get para inicializar si no existe
        totales[moneda] = totales.get(moneda, 0) + cantidad
    return totales

def calcular_balance_usd(transacciones: list) -> float:
    """
    Calcula el valor total del portafolio convertido a USD.

    Utiliza las cotizaciones actuales para determinar el valor de cada activo.

    Args:
        transacciones (list): Una lista de diccionarios con las transacciones realizadas.

    Returns:
        float: El valor total del portafolio en USD.
    """
    # Lógica: Sumar (cantidad * precio_actual) para cada transacción
    return sum(
        t['cantidad'] * obtener_valor_actual(t['moneda']) 
        for t in transacciones 
    ) # Uso de List Comprehension