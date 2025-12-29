# Diccionario simulado de precios actuales (en un caso real, usaríamos una API que acceda a datos en tiempo real)
# Ejemplos de APIs: CoinGecko, CoinMarketCap, etc.
COTIZACIONES = {
    "BTC": 65000.0, # Precio simulado de Bitcoin en USD
    "ETH": 3500.0,  # Precio simulado de Ethereum en USD
    "SOL": 140.0,   # Precio simulado de Solana en USD
    "USDT": 1.0     # Precio simulado de Tether en USD
}

def obtener_valor_actual(moneda: str) -> float:
    """Devuelve el valor actual de una moneda o 0.0 si no existe."""
    return COTIZACIONES.get(moneda.upper(), 0.0) # Se utiliza get para evitar KeyError en el diccionario

def calcular_totales(transacciones: list) -> dict:
    """
    Recibe una lista de diccionarios con transacciones.
    Devuelve un diccionario con el total acumulado por moneda.
    Ej: [{'moneda': 'BTC', 'cantidad': 0.5}, ...] -> {'BTC': 1.2, ...}
    """
    totales = {}
    for t in transacciones:         # Lista de diccionarios
        moneda = t['moneda']
        cantidad = t['cantidad']
        
        # Uso de get para inicializar si no existe
        totales[moneda] = totales.get(moneda, 0) + cantidad
    return totales

def calcular_balance_usd(transacciones: list) -> float:
    """Calcula el valor total del portafolio en USD usando List Comprehension."""
    # Lógica: Sumar (cantidad * precio_actual) para cada transacción
    return sum(
        t['cantidad'] * obtener_valor_actual(t['moneda']) 
        for t in transacciones 
    ) # Uso de List Comprehension