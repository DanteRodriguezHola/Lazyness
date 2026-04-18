from os import path, listdir
from PIL import Image

from tkinter import filedialog

def es_imagen(ruta_elemento):
    try:
        with Image.open(ruta_elemento) as elemento:
            elemento.verify()
            return True

    except (IOError, SyntaxError):
        return False
    
def examinar_elementos(carpeta):
    elementos_encontrados = listdir(carpeta)
    imagenes_encontradas = []
    
    for elemento in elementos_encontrados:
        ruta_elemento = path.join(carpeta, elemento)
        
        if es_imagen(ruta_elemento):
            imagenes_encontradas.append(ruta_elemento)
            
    return imagenes_encontradas

carpeta = filedialog.askdirectory()
print(examinar_elementos(carpeta))
        
        