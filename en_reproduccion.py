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

class Trafico:
    def __init__(self):
        self.trafico_base = []
        self.trafico_reproduccion = []
        self.posicion_actual = 0

    def anterior_cancion(self):
        if self.posicion_actual <= 0:
            return
        
        self.posicion_actual -= 1
        os.system("cls")
        print(f"Cancion actual: {os.path.basename(self.trafico_reproduccion[self.posicion_actual])}") 

    def siguiente_cancion(self):
        if self.posicion_actual >= len(self.trafico_reproduccion) - 1:
            return
        
        self.posicion_actual += 1
        os.system("cls")
        print(f"Cancion actual: {os.path.basename(self.trafico_reproduccion[self.posicion_actual])}")

    def reproducir_cancion(self):
        pass

    def añadir_carpeta(self):
        nuevos_archivos = abrir_carpeta()

        self.trafico_reproduccion.extend(nuevos_archivos)
        
class EnReproduccion:
    def __init__(self):
        root = Tk()
        root.title("Lazyness")
        root.geometry("800x600")
        root.resizable(False, False)

        mainframe = ttk.Frame(root, width = 800, height = 600)
        mainframe.grid(column = 1, row = 1)

        trafico = Trafico()
        trafico.añadir_carpeta()

        # === FRAME DE LOS METADATOS ===

        cancion = trafico.trafico_reproduccion[trafico.posicion_actual]
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
        self.label_titulo = ttk.Label(frame_metadatos, textvariable = titulo)
        self.label_titulo["font"] = "TkHeadingFont:"
        self.label_titulo.grid(column = 1, row = 2)

        artista = StringVar(value = metadatos.artist)
        self.label_artista = ttk.Label(frame_metadatos, textvariable = artista)
        self.label_artista.grid(column = 1, row = 3)

        album = StringVar(value = metadatos.album)
        self.label_album = ttk.Label(frame_metadatos, textvariable = album)
        self.label_album.grid(column = 1, row = 4)

        # === FRAME DE LOS METADATOS ===

        # === FRAME DE LOS CONTROLES ===

        frame_controles = ttk.Frame(mainframe, width = 800, height = 250)
        frame_controles["padding"] = 5
        frame_controles["relief"] = "sunken"
        frame_controles.grid(column = 1, row = 2)
        
            # === CREACIÓN DE LOS CONTROLES ===

        control_posicion = ttk.Scale(frame_controles, length = 750, from_= 0, to = 100)
        control_posicion.grid(column = 1, columnspan = 7, row = 1)

        boton_anterior = ttk.Button(frame_controles, text = "◀|")
        boton_anterior["command"] = trafico.anterior_cancion
        boton_anterior.grid(column = 1, row = 3)

        boton_retroceder = ttk.Button(frame_controles, text = "◀◀")
        boton_retroceder.grid(column = 2, row = 3)

        estado = StringVar(value = "I I")
        boton_estado = ttk.Button(frame_controles, textvariable = estado)
        boton_estado.grid(column = 3, row = 3)

        boton_stop = ttk.Button(frame_controles, text = "■")
        boton_stop.grid(column = 4, row = 3)

        boton_retroceder = ttk.Button(frame_controles, text = "▶▶")
        boton_retroceder.grid(column = 5, row = 3)

        boton_siguente = ttk.Button(frame_controles, text = "|▶")
        boton_siguente["command"] = trafico.siguiente_cancion
        boton_siguente.grid(column = 6, row = 3)

        control_volumen = ttk.Scale(frame_controles, length = 150, from_ = 0, to = 9)
        control_volumen.grid(column = 7, row = 3)

            # === CREACIÓN DE LOS CONTROLES ===

        # === FRAME DE LOS BOTONES ===

        root.mainloop()

    def obtener_caratula(self, cancion):
        carpeta = os.path.dirname(cancion)
        nombre_caratula = "cover.png"

        ruta_caratula = os.path.join(carpeta, nombre_caratula)
        return ruta_caratula


ahora = EnReproduccion()