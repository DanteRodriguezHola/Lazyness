from tkinter import filedialog, messagebox
from os import path, listdir

def es_audio(elemento):
    if elemento.endswith(".mp3"):
        return True

    if elemento.endswith(".flac"):
        return True

    return False   

def examinar_elementos(carpeta):
    elementos_encontrados = listdir(carpeta)

    canciones_encontradas = []
    subcarpetas_encontradas = []

    for elemento in elementos_encontrados:
        ruta_elemento = path.join(carpeta, elemento)

        if path.isdir(ruta_elemento):
            subcarpetas_encontradas.append(ruta_elemento)

        elif es_audio(ruta_elemento):
            canciones_encontradas.append(ruta_elemento)

    return canciones_encontradas, subcarpetas_encontradas

def examinar_carpetas(carpeta_padre):
    carpetas_restantes = [carpeta_padre]
    canciones_total = []

    while carpetas_restantes:
        carpeta_actual = carpetas_restantes[0]
        canciones, subcarpetas = examinar_elementos(carpeta_actual)

        carpetas_restantes.extend(subcarpetas)
        canciones_total.extend(canciones)
        
        carpetas_restantes.remove(carpeta_actual)

    return canciones
        
def abrir_carpeta():
    carpeta = filedialog.askdirectory()
    canciones = examinar_carpetas(carpeta)

    return canciones