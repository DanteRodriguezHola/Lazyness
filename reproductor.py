from tkinter import *
from tkinter import ttk
from tinytag import TinyTag
from os import path
from PIL import ImageTk, Image

from abrir_carpeta import abrir_carpeta
from cola import mixer
import cola as cola

class Reproductor:
    def __init__(self):
        root = Tk()
        root.title("Rogilla")
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

        ruta_caratula = "no cover.png"

        self.caratula = ImageTk.PhotoImage(file = ruta_caratula)
        self.label_caratula = ttk.Label(frame_caratula, image = self.caratula)
        self.label_caratula.grid(column = 1, row = 1)

        # === FRAME DE LA CARÁTULA ===

        # === FRAME DE LOS DETALLES ===

        frame_detalles = ttk.Frame(mainframe, width = 300, height = 300)
        frame_detalles["padding"] = 10
        frame_detalles["relief"] = "sunken"
        frame_detalles.grid(column = 2, row = 1)

        self.titulo = StringVar(value = "Titulo desconocido")
        label_titulo = ttk.Label(frame_detalles,textvariable = self.titulo, width = 29)
        label_titulo["anchor"] = "center"
        label_titulo["font"] = "TkHeadingFont:"
        label_titulo.grid(column = 1, row = 2)

        self.artista = StringVar(value = "Artista desconocido")
        label_artista = ttk.Label(frame_detalles, textvariable = self.artista)
        label_artista["anchor"] = "center"
        label_artista.grid(column = 1, row = 3)

        self.album = StringVar(value = "Álbum desconocido")
        label_album = ttk.Label(frame_detalles, textvariable = self.album)
        label_album["anchor"] = "center"
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
        
        self.conseguir_caratula()

    def conseguir_ruta_caratula(self):
        ruta_carpeta = path.dirname(cola.cancion_actual)
        nombre_caratula = "front.jpg"

        ruta_caratula = path.join(ruta_carpeta, nombre_caratula)

        return ruta_caratula

    def conseguir_caratula(self):
        ruta_caratula = self.conseguir_ruta_caratula()

        caratula = Image.open(ruta_caratula)
        caratula = caratula.resize((500, 500))

        self.caratula = ImageTk.PhotoImage(caratula)
        self.label_caratula.configure(image = self.caratula)


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
        cola.cantidad_canciones = len(cola.cola_reproduccion) - 1

        if cola.posicion_actual >= cola.cantidad_canciones:
            return
        
        cola.posicion_actual += 1
        self.actualizar_cancion_actual()

        if cola.estado == cola.REPRODUCCION:
            self.reproducir_cancion()

        elif cola.estado == cola.PAUSA:
            self.actualizar_metadatos()
            
    def pausar_cancion(self):
        mixer.music.pause()
        cola.estado = cola.PAUSA
        self.estado.set("▶")
        
    def reanudar_cancion(self):
        mixer.music.unpause()
        cola.estado = cola.REPRODUCCION
        self.estado.set("▮▮")
        
    def cambiar_estado(self):
        if cola.estado == cola.REPRODUCCION:
            self.pausar_cancion()

        elif cola.estado == cola.PAUSA:
            self.reanudar_cancion()

        self.boton_detener["state"] = "normal"

    def detener_cancion(self):
        mixer.music.set_pos(0.00)
        self.boton_detener["state"] = "disabled"

        mixer.music.pause()
        self.estado.set("▶")
        cola.estado = cola.PAUSA
    
    def redondear_volumen(self, valor_volumen):
        valor_volumen = float(valor_volumen)
        volumen_redondeado = round(valor_volumen, 2)
        
        return volumen_redondeado
    
    def cambiar_volumen(self, valor_volumen):
        volumen_redondeado = self.redondear_volumen(valor_volumen)
        nuevo_volumen = volumen_redondeado / 10

        mixer.music.set_volume(nuevo_volumen)
        self.volumen.set(volumen_redondeado)

Reproductor()