"""
Módulo para la gestión de persistencia de datos.

Se encarga de cargar y guardar la información de la cartera en un archivo JSON
utilizando la biblioteca pathlib para la gestión de rutas.
"""

import json
from pathlib import Path

# Definimos la ruta como un objeto Path
ARCHIVO_DATOS = Path("cartera.json")

def cargar_datos() -> list:
    """
    Carga la lista de transacciones desde el archivo JSON de datos.

    Returns:
        list: Una lista de transacciones. Devuelve una lista vacía si el archivo
              no existe o si ocurre un error durante la lectura.
    """
    # Método orientado a objetos para comprobar existencia
    if not ARCHIVO_DATOS.exists():
        return []
    
    try:
        # Path tiene su propio método .open(), que actúa igual que open()
        with ARCHIVO_DATOS.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def guardar_datos(datos: list):
    """
    Guarda la lista de transacciones proporcionada en el archivo JSON.

    Args:
        datos (list): La lista de transacciones a persistir.
    """
    try:
        # Escritura usando el método del objeto Path
        with ARCHIVO_DATOS.open("w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)
        print("Datos guardados correctamente.")
    except IOError:
        print("Error al guardar los datos.")