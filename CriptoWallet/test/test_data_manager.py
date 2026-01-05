import json
import pytest
from pathlib import Path
from app.data_magaer import cargar_datos, guardar_datos

@pytest.fixture
def temp_data_file(tmp_path, monkeypatch):
    """Fixture que crea un archivo temporal para las pruebas de datos."""
    d = tmp_path / "test_cartera.json"
    monkeypatch.setattr("app.data_magaer.ARCHIVO_DATOS", d)
    return d

def test_cargar_datos_archivo_no_existe(temp_data_file):
    """Prueba que cargar_datos devuelva una lista vacía si el archivo no existe."""
    # temp_data_file no existe aún
    assert cargar_datos() == []

def test_guardar_y_cargar_datos(temp_data_file):
    """Prueba que los datos se guarden y carguen correctamente."""
    datos = [{"moneda": "BTC", "cantidad": 1.2}]
    guardar_datos(datos)
    
    # Verificar que el archivo se creó
    assert temp_data_file.exists()
    
    # Verificar que los datos cargados coinciden
    cargados = cargar_datos()
    assert cargados == datos

def test_cargar_datos_corruptos(temp_data_file):
    """Prueba que cargar_datos maneje archivos JSON corruptos."""
    temp_data_file.write_text("invalid json")
    assert cargar_datos() == []
