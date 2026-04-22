from tkinter import filedialog, messagebox
from os import path, listdir
import fleep

import cola
def es_audio(ruta_archivo):
    with open(ruta_archivo, "rb") as archivo:
        tipo_archivo = fleep.get(archivo.read(128))
        if tipo_archivo.type == ["audio"]:
            return True
        
        else:
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

    return canciones_total
        
def abrir_carpeta():
    carpeta = filedialog.askdirectory()
    canciones = examinar_carpetas(carpeta)

    return canciones

def examinar_playlist(ruta_playlist):
    canciones = []

    with open(ruta_playlist, "r") as playlist:
        contenido = playlist.readlines()

        for elemento in contenido:
            elemento_limpio = elemento.rstrip("\n")

            if not path.exists(elemento_limpio):
                continue
            
            if not es_audio(elemento_limpio):
                continue

            canciones.append(elemento_limpio)

    return canciones

def abrir_playlist():
    formatos = "*.m3u *.m3u8"

    ruta_playlist = filedialog.askopenfilename(title = "Seleccione una playlist", filetypes = [("Playlists", formatos)])
    return ruta_playlist

def leer_playlist():
    ruta_playlist = abrir_playlist()
    canciones = examinar_playlist(ruta_playlist)

    return canciones