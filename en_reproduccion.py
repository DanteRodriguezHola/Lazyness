from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os

def armar_ruta_archivo(carpeta, archivo):
    ruta_archivo = os.path.join(carpeta, archivo)
    return ruta_archivo

def filtrar_archivos(carpeta):
    archivos = os.listdir(carpeta)
    archivos_filtrados = []

    for archivo in archivos:
        if archivo.endswith(".mp3") or archivo.endswith(".flac"):
            ruta_archivo = armar_ruta_archivo(carpeta, archivo)
            archivos_filtrados.append(ruta_archivo)

    return archivos_filtrados

def abrir_carpeta():
    carpeta = filedialog.askdirectory()
    archivos = filtrar_archivos(carpeta)

class EnReproduccion:
    def __init__(self):
        root = Tk()
        root.title("Lazyness")
        root.geometry("800x600")
        root.resizable(False, False)

        mainframe = ttk.Frame(root, width = 800, height = 600)
        mainframe.grid(column = 1, row = 1)

        # === FRAME DE LOS METADATOS ===

        frame_metadatos = ttk.Frame(mainframe, width= 800, height = 450)
        frame_metadatos["padding"] = 10
        frame_metadatos["relief"] = "sunken"
        frame_metadatos.grid(column = 1, row = 1)

        caratula = PhotoImage(file = "no_cover.png")
        label_caratula = ttk.Label(frame_metadatos, image = caratula)
        label_caratula.grid(column = 1, row = 1)

        titulo = StringVar(value = "<titulo de la cancion>")
        label_titulo = ttk.Label(frame_metadatos, textvariable = titulo)
        label_titulo["font"] = "TkHeadingFont:"
        label_titulo.grid(column = 1, row = 2)

        artista = StringVar(value = "<artista de la cancion>")
        label_artista = ttk.Label(frame_metadatos, textvariable = artista)
        label_artista.grid(column = 1, row = 3)

        album = StringVar(value = "<titulo del album>")
        label_album = ttk.Label(frame_metadatos, textvariable = album)
        label_album.grid(column = 1, row = 4)

        # === FRAME DE LOS CONTROLES ===

        frame_controles = ttk.Frame(mainframe, width = 800, height = 250)
        frame_controles["relief"] = "sunken"
        frame_controles.grid(column = 1, row = 2)

        root.mainloop()

abrir_carpeta()
ahora = EnReproduccion()