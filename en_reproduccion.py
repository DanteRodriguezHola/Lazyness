from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tinytag import TinyTag

from abrir_carpeta import abrir_carpeta

import reproductor as r
from reproductor import mixer

root = Tk()
root.title("Lazyness")
root.geometry("800x600")
root.resizable(False, False)

mainframe = ttk.Frame(root, width = 800, height = 600)
mainframe["padding"] = 10
mainframe.grid(column = 1, row = 1)

# === FUNCIONES DE REPRODUCCIÓN ===

def actualizar_metadatos(cancion):
    metadatos = TinyTag.get(cancion)

    titulo.set(metadatos.title)
    artista.set(metadatos.artist)
    album.set(metadatos.album)

def reproducir_cancion():
    if r.cancion_actual:
        mixer.music.load(r.cancion_actual)
        mixer.music.play()

        actualizar_metadatos(r.cancion_actual)

def siguente_cancion():
    cantidad_canciones = len(r.cola_reproduccion) - 1

    if r.posicion_actual >= cantidad_canciones:
        return
    
    r.posicion_actual += 1
    r.cancion_actual = r.cola_reproduccion[r.posicion_actual]

    reproducir_cancion()

def cambiar_estado(boton):
    if r.estado == r.REPRODUCCION:
        mixer.music.pause()
        boton.config(text = "▶")

    elif r.estado == r.PAUSA:
        mixer.music.unpause()
        boton.config(text = "I I")

    r.estado = not(r.estado)

def detener_cancion(boton):
    mixer.music.set_pos(0.00)
    r.estado == r.PAUSA

    cambiar_estado(boton)

# === FUNCIONES DE REPRODUCCIÓN ===

# === FRAME DE LA CARÁTULA ===

canciones = abrir_carpeta()

r.cola_reproduccion.extend(canciones)

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

titulo = StringVar(value = "Titulo desconocido")
label_titulo = ttk.Label(frame_detalles,textvariable = titulo)
label_titulo["font"] = "TkHeadingFont:"
label_titulo.grid(column = 1, row = 2)

artista = StringVar(value = "Artista desconocido")
label_artista = ttk.Label(frame_detalles, textvariable = artista)
label_artista.grid(column = 1, row = 3)

album = StringVar(value = "Álbum desconocido")
label_album = ttk.Label(frame_detalles, textvariable = album)
label_album.grid(column = 1, row = 4)

# === FRAME DE LOS DETALLES ===

# === FRAME DE LOS CONTROLES ===

frame_controles = ttk.Frame(mainframe, width = 300, height = 300)
frame_controles["padding"] = 5
frame_controles["relief"] = "sunken"
frame_controles.grid(column = 2, row = 2)

    # === CREACIÓN DE LOS CONTROLES ===

control_posicion = ttk.Scale(frame_controles, length = 300, from_= 0, to = 100)
control_posicion.grid(column = 1, columnspan = 7, row = 1)

boton_anterior = ttk.Button(frame_controles, text = "◀|", width = 4)
boton_anterior.grid(column = 1, row = 3)

boton_retroceder = ttk.Button(frame_controles, text = "◀◀", width = 4)
boton_retroceder.grid(column = 2, row = 3)

boton_estado = ttk.Button(frame_controles, text = "I I", width = 4)
boton_estado["command"] = lambda boton = boton_estado: cambiar_estado(boton)
boton_estado.grid(column = 3, row = 3)

boton_stop = ttk.Button(frame_controles, text = "■", width = 4)
boton_stop["command"] = lambda boton = boton_estado: detener_cancion(boton)
boton_stop.grid(column = 4, row = 3)

boton_retroceder = ttk.Button(frame_controles, text = "▶▶", width = 4)
boton_retroceder.grid(column = 5, row = 3)

boton_siguente = ttk.Button(frame_controles, text = "|▶", width = 4)
boton_siguente["command"] = siguente_cancion
boton_siguente.grid(column = 6, row = 3)

control_volumen = ttk.Scale(frame_controles, length = 150, from_ = 0, to = 9)
control_volumen.grid(column = 1, columnspan = 6, row = 4)

    # === CREACIÓN DE LOS CONTROLES ===

boton_abrir_carpeta = ttk.Button(frame_controles, text = "Abrir carpeta")
boton_abrir_carpeta["command"] = abrir_carpeta
boton_abrir_carpeta.grid(column = 1, row = 5)

# === FRAME DE LOS BOTONES ===

reproducir_cancion()

root.mainloop()