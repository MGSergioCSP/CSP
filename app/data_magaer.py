import json
from pathlib import Path

# Definimos la ruta como un objeto Path
ARCHIVO_DATOS = Path("cartera.json")

def cargar_datos() -> list:
    """
    Carga la cartera desde un archivo JSON. 
    Devuleve una lista vacía si no existe o el archivo está corrupto.
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
    """Guarda la lista de transacciones en el archivo JSON."""
    try:
        # Escritura usando el método del objeto Path
        with ARCHIVO_DATOS.open("w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)
        print("Datos guardados correctamente.")
    except IOError:
        print("Error al guardar los datos.")