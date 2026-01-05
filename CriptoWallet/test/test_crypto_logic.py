import pytest
from app.crypto_logic import obtener_valor_actual, calcular_totales, calcular_balance_usd

def test_obtener_valor_actual():
    """Prueba que se obtenga el valor correcto para una moneda existente y 0.0 para una inexistente."""
    assert obtener_valor_actual("BTC") == 65000.0
    assert obtener_valor_actual("eth") == 3500.0
    assert obtener_valor_actual("XYZ") == 0.0

def test_calcular_totales():
    """Prueba que el cálculo de totales por moneda sea correcto."""
    transacciones = [
        {"moneda": "BTC", "cantidad": 0.5},
        {"moneda": "ETH", "cantidad": 2.0},
        {"moneda": "BTC", "cantidad": 0.3},
    ]
    resultado = calcular_totales(transacciones)
    assert resultado["BTC"] == 0.8
    assert resultado["ETH"] == 2.0
    assert len(resultado) == 2

def test_calcular_balance_usd():
    """Prueba que el cálculo del balance total en USD sea correcto."""
    transacciones = [
        {"moneda": "BTC", "cantidad": 1.0}, # 65000
        {"moneda": "USDT", "cantidad": 500.0}, # 500
    ]
    # 1.0 * 65000 + 500.0 * 1.0 = 65500.0
    assert calcular_balance_usd(transacciones) == 65500.0
