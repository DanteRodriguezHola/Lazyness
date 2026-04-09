from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tinytag import TinyTag

import os


def filtrar_archivos(carpeta):
    archivos = os.listdir(carpeta)
    archivos_filtrados = []
    carpetas_encontradas = []

    for archivo in archivos:
        ruta_archivo = os.path.join(carpeta, archivo)

        if os.path.isdir(ruta_archivo):
            carpetas_encontradas.append(ruta_archivo)

        elif archivo.endswith(".mp3") or archivo.endswith(".flac"):
            archivos_filtrados.append(ruta_archivo)

    return carpetas_encontradas, archivos_filtrados

def recorrer_carpetas(carpeta):
    carpetas_restantes = [carpeta]
    archivos_encontrados = []

    while carpetas_restantes:
        carpeta_actual = carpetas_restantes[0]
        carpetas_encontradas, archivos_filtrados = filtrar_archivos(carpeta_actual)

        if carpetas_encontradas:
            carpetas_restantes.extend(carpetas_encontradas)
        
        archivos_encontrados.extend(archivos_filtrados)
        carpetas_restantes.remove(carpeta_actual)

    return archivos_encontrados

def abrir_carpeta():
    carpeta = filedialog.askdirectory()
    archivos = recorrer_carpetas(carpeta)

    for archivo in archivos:
        print(archivo)

    return archivos

"""
class Cola:
    def __init__(self):
        self.cola_base = []
        self.cola_reproduccion = []
"""

class EnReproduccion:
    def __init__(self):
        root = Tk()
        root.title("Lazyness")
        root.geometry("800x600")
        root.resizable(False, False)

        mainframe = ttk.Frame(root, width = 800, height = 600)
        mainframe.grid(column = 1, row = 1)

        carpeta = abrir_carpeta()
        cancion = carpeta[0]

        # === FRAME DE LOS METADATOS ===

        metadatos = TinyTag.get(cancion)

        frame_metadatos = ttk.Frame(mainframe, width= 800, height = 450)
        frame_metadatos["padding"] = 10
        frame_metadatos["relief"] = "sunken"
        frame_metadatos.grid(column = 1, row = 1)

        ruta_caratula = self.obtener_caratula(cancion)

        caratula = PhotoImage(file = ruta_caratula)
        label_caratula = ttk.Label(frame_metadatos, image = caratula)
        label_caratula.grid(column = 1, row = 1)

        titulo = StringVar(value = metadatos.title)
        label_titulo = ttk.Label(frame_metadatos, textvariable = titulo)
        label_titulo["font"] = "TkHeadingFont:"
        label_titulo.grid(column = 1, row = 2)

        artista = StringVar(value = metadatos.artist)
        label_artista = ttk.Label(frame_metadatos, textvariable = artista)
        label_artista.grid(column = 1, row = 3)

        album = StringVar(value = metadatos.album)
        label_album = ttk.Label(frame_metadatos, textvariable = album)
        label_album.grid(column = 1, row = 4)

        # === FRAME DE LOS CONTROLES ===

        frame_controles = ttk.Frame(mainframe, width = 800, height = 250)
        frame_controles["relief"] = "sunken"
        frame_controles.grid(column = 1, row = 2)

        root.mainloop()

    def obtener_caratula(self, cancion):
        carpeta = os.path.dirname(cancion)
        nombre_caratula = "cover.png"

        ruta_caratula = os.path.join(carpeta, nombre_caratula)
        return ruta_caratula


ahora = EnReproduccion()