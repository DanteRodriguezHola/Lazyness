from os import path, listdir
from pathlib import Path
from PIL import Image
from tkinter import filedialog

import cola

def es_imagen(ruta_elemento):
    try:
        with Image.open(ruta_elemento) as elemento:
            elemento.verify()
            return True

    except (IOError, SyntaxError):
        return False

"""
def examinar_elementos(carpeta):
    elementos_encontrados = listdir(carpeta)
    imagenes_encontradas = []
    
    for elemento in elementos_encontrados:
        ruta_elemento = path.join(carpeta, elemento)
        
        if es_imagen(ruta_elemento):
            imagenes_encontradas.append(ruta_elemento)
            
    return imagenes_encontradas

def clasificar_caratulas(imagenes, caratulas):
    nombre_caratula_single = Path(cola.cancion_actual).stem
    
    nombres_caratula_frontal = [
        "cover",
        "front",
        "front cover",
        "artwork",
        "album art",
        "folder"
        ]
    
    nombres_caratula_trasera = "back"
    
    for imagen in imagenes:
        nombre_imagen = Path(imagen).stem
        
        if nombre_imagen == nombre_caratula_single:
            caratulas["single"] = imagen
            
        elif nombre_imagen in nombres_caratula_frontal:
            caratulas["frontal"] = imagen
            
        elif nombre_imagen in nombres_caratula_trasera:
            caratulas["trasera"] = imagen
            
    return caratulas

def redimensionar_caratula(caratula):
    caratula = Image.open(caratula)
    caratula = caratula.resize((500, 500))
    
    return caratula

def asignar_caratulas(imagenes):
    caratulas_posibles = {
        "single": None,
        "frontal": None,
        "trasera": None
        }
    
    caratulas_encontradas = []
    
    caratulas_posibles = clasificar_caratulas(imagenes, caratulas_posibles)
    
    for caratula in caratulas_posibles.values():
        if caratula:
            caratula = redimensionar_caratula(caratula)
            caratulas_encontradas.append(caratula)
            
    return caratulas_encontradas

def obtener_caratulas():
    carpeta = path.dirname(cola.cancion_actual)
    imagenes = examinar_elementos(carpeta)
    
    if imagenes:
        caratulas = asignar_caratulas(imagenes)
        
    return caratulas

caratulas = []
cantidad_caratulas = len(caratulas) -1
posicion_actual = 0
"""

def obtener_imagen_caratula():
    imagen_default= Image.open("default.png")
    
    if not cola.cancion_actual:
        return imagen_default
    
    ruta_carpeta = path.dirname(cola.cancion_actual)
    elementos_encontrados = listdir(ruta_carpeta)
    nombre_caratula = "front.jpg"
    
    if not nombre_caratula in elementos_encontrados:
        return imagen_default
    
    ruta_caratula = path.join(ruta_carpeta, nombre_caratula)
    imagen_caratula = Image.open(ruta_caratula)
    imagen_caratula = imagen_caratula.resize((500, 500))
    
    return imagen_caratula