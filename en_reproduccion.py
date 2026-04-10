from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tinytag import TinyTag

root = Tk()
root.title("Lazyness")
root.geometry("800x600")
root.resizable(False, False)

mainframe = ttk.Frame(root, width = 800, height = 600)
mainframe.grid(column = 1, row = 1)

# === FRAME DE LA CARÁTULA ===

cancion = "C:/Users/Public/Music/2026.01.15 - Eyeball/01 - Eyeball.flac"
metadatos = TinyTag.get(cancion)

frame_caratula = ttk.Frame(mainframe, width = 500, height = 600)
frame_caratula.grid(column = 1, row = 1, rowspan = 2)


ruta_caratula = "C:/Users/Public/Music/2026.01.15 - Eyeball/cover.png"

caratula = PhotoImage(file = ruta_caratula)
label_caratula = ttk.Label(frame_caratula, image = caratula)
label_caratula.grid(column = 1, row = 1)

# === FRAME DE LA CARÁTULA ===

# === FRAME DE LOS DETALLES ===

frame_detalles = ttk.Frame(mainframe, width = 300, height = 300)
frame_detalles["padding"] = 10
frame_detalles["relief"] = "sunken"
frame_detalles.grid(column = 2, row = 1)

titulo = StringVar(value = metadatos.title)
label_titulo = ttk.Label(frame_detalles, textvariable = titulo)
label_titulo["font"] = "TkHeadingFont:"
label_titulo.grid(column = 1, row = 2)

artista = StringVar(value = metadatos.artist)
label_artista = ttk.Label(frame_detalles, textvariable = artista)
label_artista.grid(column = 1, row = 3)

album = StringVar(value = metadatos.album)
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

boton_anterior = ttk.Button(frame_controles, text = "◀|", width = 2)
boton_anterior.grid(column = 1, row = 3)

boton_retroceder = ttk.Button(frame_controles, text = "◀◀", width = 2)
boton_retroceder.grid(column = 2, row = 3)

estado = StringVar(value = "I I")
boton_estado = ttk.Button(frame_controles, textvariable = estado, width = 2)
boton_estado.grid(column = 3, row = 3)

boton_stop = ttk.Button(frame_controles, text = "■", width = 2)
boton_stop.grid(column = 4, row = 3)

boton_retroceder = ttk.Button(frame_controles, text = "▶▶", width = 2)
boton_retroceder.grid(column = 5, row = 3)

boton_siguente = ttk.Button(frame_controles, text = "|▶", width = 2)
boton_siguente.grid(column = 6, row = 3)

control_volumen = ttk.Scale(frame_controles, length = 150, from_ = 0, to = 9)
control_volumen.grid(column = 7, row = 3)

    # === CREACIÓN DE LOS CONTROLES ===

# === FRAME DE LOS BOTONES ===

root.mainloop()