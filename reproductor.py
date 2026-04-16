from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tinytag import TinyTag

from abrir_carpeta import abrir_carpeta

import cola as cola
from cola import mixer

class Reproductor:
    def __init__(self):
        root = Tk()
        root.title("Lazyness")
        root.geometry("800x600")
        root.resizable(False, False)

        mainframe = ttk.Frame(root, width = 800, height = 600)
        mainframe["padding"] = 10
        mainframe.grid(column = 1, row = 1)

        # === FRAME DE LA CARÁTULA ===

        canciones = abrir_carpeta()

        cola.cola_reproduccion.extend(canciones)

        frame_caratula = ttk.Frame(mainframe, width = 500, height = 600)
        frame_caratula.grid(column = 1, row = 1, rowspan = 2)

        ruta_caratula = "no_cover.png"

        caratula = PhotoImage(file = ruta_caratula)
        label_caratula = ttk.Label(frame_caratula, image = caratula)
        label_caratula.grid(column = 1, row = 1)

        # === FRAME DE LA CARÁTULA ===

        # === FRAME DE LOS DETALLES ===

        frame_detalles = ttk.Frame(mainframe, width = 300, height = 300)
        frame_detalles["padding"] = 10
        frame_detalles["relief"] = "sunken"
        frame_detalles.grid(column = 2, row = 1)

        self.titulo = StringVar(value = "Titulo desconocido")
        label_titulo = ttk.Label(frame_detalles,textvariable = self.titulo)
        label_titulo["font"] = "TkHeadingFont:"
        label_titulo.grid(column = 1, row = 2)

        self.artista = StringVar(value = "Artista desconocido")
        label_artista = ttk.Label(frame_detalles, textvariable = self.artista)
        label_artista.grid(column = 1, row = 3)

        self.album = StringVar(value = "Álbum desconocido")
        label_album = ttk.Label(frame_detalles, textvariable = self.album)
        label_album.grid(column = 1, row = 4)

        # === FRAME DE LOS DETALLES ===

        # === FRAME DE LOS CONTROLES ===

        frame_controles = ttk.Frame(mainframe, width = 300, height = 300)
        frame_controles["padding"] = 5
        frame_controles["relief"] = "sunken"
        frame_controles.grid(column = 2, row = 2)

            # === CREACIÓN DE LOS CONTROLES ===

        """
        self.control_posicion = ttk.Scale(frame_controles, length = 300, from_= 0, to = 100)
        self.control_posicion.grid(column = 1, columnspan = 4, row = 1)
        """

        self.boton_anterior = ttk.Button(frame_controles, text = "◀|", width = 4)
        self.boton_anterior["command"] = self.anterior_cancion
        self.boton_anterior.grid(column = 1, row = 3)

        self.estado = StringVar(value = "▮▮")
        self.boton_estado = ttk.Button(frame_controles, textvariable = self.estado, width = 4)
        self.boton_estado["command"] = self.cambiar_estado
        self.boton_estado.grid(column = 2, row = 3)

        self.boton_detener = ttk.Button(frame_controles, text = "■", width = 4)
        self.boton_detener["command"] = self.detener_cancion
        self.boton_detener.grid(column = 3, row = 3)


        self.boton_siguente = ttk.Button(frame_controles, text = "|▶", width = 4)
        self.boton_siguente["command"] = self.siguente_cancion
        self.boton_siguente.grid(column = 4, row = 3)

        self.volumen = StringVar(value = "10")
        self.label_volumen = ttk.Label(frame_controles, textvariable = self.volumen)
        self.label_volumen.grid(column = 2, columnspan = 2, row = 5)

        self.control_volumen = ttk.Scale(frame_controles, length = 150, from_ = 0, to = 10)
        self.control_volumen.set(10)
        self.control_volumen["command"] = self.cambiar_volumen
        self.control_volumen.grid(column = 1, columnspan = 4, row = 4)


            # === CREACIÓN DE LOS CONTROLES ===

        """
        boton_abrir_carpeta = ttk.Button(frame_controles, text = "Abrir carpeta")
        boton_abrir_carpeta["command"] = abrir_carpeta
        boton_abrir_carpeta.grid(column = 1, row = 5)
        """
        # === FRAME DE LOS BOTONES ===

        root.mainloop()

    def reproducir_cancion(self):
        mixer.music.load(cola.cancion_actual)
        mixer.music.play()
        self.boton_detener["state"] = "normal"

        mixer.music.play()
        self.actualizar_metadatos()

    def actualizar_metadatos(self):
        metadatos = TinyTag.get(cola.cancion_actual)

        self.titulo.set(metadatos.title)
        self.artista.set(metadatos.artist)
        self.album.set(metadatos.album)

    def actualizar_cancion_actual(self):
        cola.cancion_actual = cola.cola_reproduccion[cola.posicion_actual]
        
    def anterior_cancion(self):
        if cola.posicion_actual <= 0:
            return
        
        cola.posicion_actual -= 1
        self.actualizar_cancion_actual()

        if cola.estado == cola.REPRODUCCION:
            self.reproducir_cancion()

        if cola.estado == cola.PAUSA:
            self.actualizar_metadatos()

    def siguente_cancion(self):
        if cola.posicion_actual >= cola.cantidad_canciones:
            return
        
        cola.posicion_actual += 1
        self.actualizar_cancion_actual()

        if cola.estado == cola.REPRODUCCION:
            self.reproducir_cancion()

        elif cola.estado == cola.PAUSA:
            self.actualizar_metadatos()

    def cambiar_estado(self):
        if cola.estado == cola.REPRODUCCION:
            mixer.music.pause()
            self.estado.set("▶")
            cola.estado = cola.PAUSA

        elif cola.estado == cola.PAUSA:
            mixer.music.unpause()
            self.estado.set("▮▮")
            cola.estado = cola.REPRODUCCION

        self.boton_detener["state"] = "normal"

    def detener_cancion(self):
        mixer.music.set_pos(0.00)
        self.boton_detener["state"] = "disabled"

        mixer.music.pause()
        self.estado.set("▶")
        cola.estado = cola.PAUSA

    def cambiar_volumen(self, valor_volumen):
        volumen_redondeado = round(float(valor_volumen), 2)
        nuevo_volumen = volumen_redondeado / 10

        mixer.music.set_volume(nuevo_volumen)
        self.volumen.set(volumen_redondeado)

Reproductor()