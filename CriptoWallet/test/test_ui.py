import pytest
from unittest.mock import patch
from io import StringIO
from app.ui import mostrar_menu, pedir_transaccion, mostrar_activos

def test_mostrar_menu():
    """Prueba que el menú se muestre correctamente."""
    with patch('sys.stdout', new=StringIO()) as fake_out:
        mostrar_menu()
        output = fake_out.getvalue()
        assert "=== CRIPTO WALLET V1.0 ===" in output
        assert "1. Registrar nueva inversión" in output

def test_pedir_transaccion():
    """Prueba la captura de una transacción con entradas válidas."""
    # Simulamos la entrada: primero la moneda, luego la cantidad
    inputs = ["btc", "0.5"]
    with patch('builtins.input', side_effect=inputs):
        resultado = pedir_transaccion()
        assert resultado == {"moneda": "BTC", "cantidad": 0.5}

def test_pedir_transaccion_con_reintento():
    """Prueba que pedir_transaccion reintente si la cantidad es inválida."""
    # Símbolo, cantidad negativa (fallo), cantidad no numérica (fallo), cantidad válida
    inputs = ["ETH", "-1", "abc", "2.5"]
    with patch('builtins.input', side_effect=inputs), \
         patch('sys.stdout', new=StringIO()) as fake_out:
        resultado = pedir_transaccion()
        assert resultado == {"moneda": "ETH", "cantidad": 2.5}
        output = fake_out.getvalue()
        assert "La cantidad debe ser positiva." in output
        assert "Por favor, introduce un número válido." in output

def test_mostrar_activos():
    """Prueba que los activos se listen correctamente."""
    resumen = {"BTC": 1.23456, "ETH": 10.0}
    with patch('sys.stdout', new=StringIO()) as fake_out:
        mostrar_activos(resumen)
        output = fake_out.getvalue()
        assert "=== ACTIVOS ===" in output
        assert "BTC  :     1.2346" in output # Redondeo y formato
        assert "ETH  :    10.0000" in output
