from tkinter import *
from tkinter import ttk
from tinytag import TinyTag
from PIL import ImageTk, Image
from random import shuffle
from os import system

from abrir_archivos import abrir_carpeta
from cola import mixer

import caratula
import cola

class Reproductor:
    def __init__(self):
        root = Tk()
        root.title("Rogilla")
        root.geometry("800x600")
        root.resizable(False, False)

        mainframe = ttk.Frame(root, width = 800, height = 600)
        mainframe["padding"] = 10
        mainframe.grid(column = 1, row = 1)
        
        canciones = abrir_carpeta()

        self.actualizar_datos_cola()

        # === DEFINICION DE LOS ESTILOS ===

        tema = "clam"

        estilo_frame = ttk.Style()
        estilo_frame.theme_use(tema)
        estilo_frame.configure("TFrame", background = "#FAC41A")

        estilo_label = ttk.Style()
        estilo_label.theme_use(tema)
        estilo_label.configure("TLabel", background = "#FAC41A", foreground = "#000000")

        estilo_boton = ttk.Style()
        estilo_boton.theme_use(tema)
        estilo_boton.configure("TButton", background = "black", foreground = "#FAC41A")
        estilo_boton.map("TButton", background=[('active','black')])

        # === DEFINICION DE LOS ESTILOS ===

        # === FRAME DE LA CARÁTULA ===

        frame_caratula = ttk.Frame(mainframe, width = 500, height = 600)
        frame_caratula.grid(column = 1, row = 1, rowspan = 2)

        nombre_caratula = "default.png"
        
        self.caratula = ImageTk.PhotoImage(file = nombre_caratula)
        self.label_caratula = ttk.Label(frame_caratula, image = self.caratula)
        self.label_caratula.grid(column = 1, row = 1)
        
        """
        self.boton_anterior_caratula = ttk.Button(frame_caratula, text = "◀", width = 2)
        self.boton_anterior_caratula["command"] = self.anterior_caratula
        self.boton_anterior_caratula.grid(column = 1, row = 2, sticky = "E")
        
        self.boton_siguente_caratula = ttk.Button(frame_caratula, text = "▶", width = 2)
        self.boton_siguente_caratula["command"] = self.siguente_caratula
        self.boton_siguente_caratula.grid(column = 2, row = 2, sticky = "W")
        """
        
        # === FRAME DE LA CARÁTULA ===

        # === FRAME DE LOS DETALLES ===
        
        frame_detalles = ttk.Frame(mainframe, width = 200, height = 200)
        frame_detalles["padding"] = 10
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

        frame_controles_reproduccion = ttk.Frame(mainframe, width = 200, height = 200)
        frame_controles_reproduccion["padding"] = 5
        frame_controles_reproduccion.grid(column = 2, row = 2)

            # === CREACIÓN DE LOS CONTROLES DE REPRODUCCION ===
        
        """
        self.control_progreso = ttk.Progressbar(frame_controles_reproduccion, length = 180, orient = "horizontal")
        self.control_progreso.grid(column = 1, columnspan = 4, row = 2)
        """
        
        self.anadir_playlist = ttk.Button(frame_controles_reproduccion, text = "+", width = 4)
        self.anadir_playlist.grid(column = 1, row = 1)

        self.string_playback = StringVar(value = "⇉")
        self.boton_playback = ttk.Button(frame_controles_reproduccion, textvariable = self.string_playback, width = 4)
        self.boton_playback["command"] = self.cambiar_playback
        self.boton_playback.grid(column = 4, row = 1)
        
        self.boton_anterior = ttk.Button(frame_controles_reproduccion, text = "◀▮", width = 4)
        self.boton_anterior["command"] = self.anterior_cancion
        self.boton_anterior.grid(column = 1, row = 3)

        self.estado = StringVar(value = "▮▮")
        self.boton_estado = ttk.Button(frame_controles_reproduccion, textvariable = self.estado, width = 4)
        self.boton_estado["command"] = self.cambiar_estado
        self.boton_estado.grid(column = 2, row = 3)

        self.boton_detener = ttk.Button(frame_controles_reproduccion, text = "■", width = 4)
        self.boton_detener["command"] = self.detener_cancion
        self.boton_detener.grid(column = 3, row = 3)


        self.boton_siguente = ttk.Button(frame_controles_reproduccion, text = "▮▶", width = 4)
        self.boton_siguente["command"] = self.siguente_cancion
        self.boton_siguente.grid(column = 4, row = 3)

        self.volumen = StringVar(value = "10")
        self.label_volumen = ttk.Label(frame_controles_reproduccion, textvariable = self.volumen)
        self.label_volumen.grid(column = 2, columnspan = 2, row = 5)

        self.control_volumen = ttk.Scale(frame_controles_reproduccion, length = 150, from_ = 0, to = 10)
        self.control_volumen.set(10)
        self.control_volumen["command"] = self.cambiar_volumen
        self.control_volumen.grid(column = 1, columnspan = 4, row = 4)


            # === CREACIÓN DE LOS CONTROLES DE REPRODUCCION ===

        # === FRAME DE LOS CONTROLES DE COLA ===

        frame_controles_cola = ttk.Frame(mainframe, width = 200, height = 200)
        frame_controles_cola["padding"] = 5
        frame_controles_cola.grid(column = 2, row = 3)

        self.boton_abrir_carpeta = ttk.Button(frame_controles_cola, text = "Abrir carpeta")
        self.boton_abrir_carpeta["command"] = self.añadir_desde_carpeta
        self.boton_abrir_carpeta.grid(column = 1, row = 1)

        self.boton_abrir_archivos = ttk.Button(frame_controles_cola, text = "Abrir archivos")
        self.boton_abrir_archivos.grid(column = 2, row = 1)

        self.boton_abrir_carpeta = ttk.Button(frame_controles_cola, text = "Abrir playlist")
        self.boton_abrir_carpeta.grid(column = 1, row = 3)

        # === FRAME DE LOS BOTONES ===

        root.mainloop()
    
    # === DEFINICIONES DE FUNCIONES ===
    
        # === FUNCIONES DE LOS METADATOS Y LAS CARATULAS ===
        
    def actualizar_metadatos(self):
        metadatos = TinyTag.get(cola.cancion_actual)

        self.titulo.set(metadatos.title)
        self.artista.set(metadatos.artist)
        self.album.set(metadatos.album)
        self.actualizar_caratula()
    
    """
    def actualizar_datos_caratula(self):
        caratula.caratulas = caratula.obtener_caratulas()
        caratula.cantidad_caratulas = len(caratula.caratulas) - 1
        caratula.posicial_actual = 0
    """
    
    def actualizar_caratula(self):        
        imagen_caratula = caratula.obtener_imagen_caratula()

        self.caratula = ImageTk.PhotoImage(imagen_caratula)
        self.label_caratula.configure(image = self.caratula)
        
    """
    def anterior_caratula(self):
        if caratula.posicion_actual <= 0:
            return
        
        caratula.posicion_actual -= 1
        
        imagen_caratula = caratula.caratulas[caratula.posicion_actual]

        self.caratula = ImageTk.PhotoImage(imagen_caratula)
        self.label_caratula.configure(image = self.caratula)

    def siguente_caratula(self):
        if caratula.posicion_actual >= caratula.cantidad_caratulas:
            return
        
        caratula.posicion_actual += 1
        
        imagen_caratula = caratula.caratulas[caratula.posicion_actual]

        self.caratula = ImageTk.PhotoImage(imagen_caratula)
        self.label_caratula.configure(image = self.caratula)
    """
    
        # === FUNCIONES DE LOS METADATOS Y LAS CARATULAS ===
        
    def reproducir_cancion(self):
        mixer.music.play()
        self.boton_detener["state"] = "normal"

    def check_song_stopped(self):
        if mixer.music.get_busy or cola.estado == cola.PAUSA:
            return
        
        if cola.posicion_actual >= cola.cantidad_canciones:
            self.detener_cancion()

        self.siguente_cancion()

    def cargar_cancion(self):
        mixer.music.load(cola.cancion_actual)
        self.check_song_position()
        self.actualizar_metadatos()

    def check_song_position(self):
        if cola.posicion_actual <= 0:
            self.boton_anterior["state"] = "disable"
        else:
            self.boton_anterior["state"] = "normal"

        if cola.posicion_actual >= cola.cantidad_canciones:
            self.boton_siguente["state"] = "disable"
        else:
            self.boton_siguente["state"] = "normal"
    
    """
    def actualizar_progeso(self):
        progreso_actual = self.control_progreso["value"]

        if progreso_actual
    """

    def actualizar_cancion_actual(self):
        cola.cancion_actual = cola.cola_reproduccion[cola.posicion_actual]

    def añadir_desde_carpeta(self):
        canciones = abrir_carpeta()

        cola.cola_base = canciones
        cola.cola_reproduccion = canciones

        self.actualizar_datos_cola()
        cola.posicion_actual = 0
        # === FUNCIONES DE LA COLA ===

    def actualizar_datos_cola(self):
        cola.cantidad_canciones = len(cola.cola_reproduccion) - 1

    def aleatorizar_cola(self):
        cola.cola_reproduccion.remove(cola.cancion_actual)
        shuffle(cola.cola_reproduccion)
        cola.posicion_actual = 0
        cola.cola_reproduccion.insert(0, cola.cancion_actual)

    def normalizar_cola(self):
        cola.cola_reproduccion = cola.cola_base.copy()
        cola.posicion_actual = cola.cola_reproduccion.index(cola.cancion_actual)

    def cambiar_playback(self):
        if cola.playback == cola.NORMAL:
            self.aleatorizar_cola()
            cola.playback = cola.ALEATORIO
            self.string_playback.set("⇆")

        elif cola.playback == cola.ALEATORIO:
            self.normalizar_cola()
            cola.playback = cola.NORMAL
            self.string_playback.set("⇉")

        self.check_song_position()

        # === FUNCIONES DE LA COLA ===

        # === FUNCIONES DE LOS CONTROLES DE POSICION ===

    def anterior_cancion(self):
        cola.posicion_actual -= 1
        self.actualizar_cancion_actual()
        self.cargar_cancion()

        if cola.estado == cola.REPRODUCCION:
            self.reproducir_cancion()

    def siguente_cancion(self):
        cola.posicion_actual += 1
        self.actualizar_cancion_actual()
        self.cargar_cancion()

        if cola.estado == cola.REPRODUCCION:
            self.reproducir_cancion()
            
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

        # === FUNCIONES DE LOS CONTROLES DE POSICION ===

        # === FUNCION DEL CONTROLADOR DE VOLUMEN ===

    def redondear_volumen(self, valor_volumen):
        valor_volumen = float(valor_volumen)
        volumen_redondeado = round(valor_volumen, 2)
        
        return volumen_redondeado
    
    def cambiar_volumen(self, valor_volumen):
        volumen_redondeado = self.redondear_volumen(valor_volumen)
        nuevo_volumen = volumen_redondeado / 10

        mixer.music.set_volume(nuevo_volumen)
        self.volumen.set(volumen_redondeado)

        # === FUNCIONES DEL CONTROLADOR DE VOLUMEN ===

    # === DEFINICIONES DE FUNCIONES ===
Reproductor()