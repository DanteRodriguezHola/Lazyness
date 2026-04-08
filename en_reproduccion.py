from tkinter import *
from tkinter import ttk

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
        frame_metadatos["relief"] = "sunken"
        frame_metadatos.grid(column = 1, row = 1)

        # === FRAME DE LOS CONTROLES ===

        frame_controles = ttk.Frame(mainframe, width = 800, height = 250)
        frame_controles["relief"] = "sunken"
        frame_controles.grid(column = 1, row = 2)

        root.mainloop()

ahora = EnReproduccion()