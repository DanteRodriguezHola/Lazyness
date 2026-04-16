from pygame import mixer
from abrir_carpeta import abrir_carpeta

mixer.init()

REPRODUCCION = False
PAUSA = True

cola_base = []
cola_reproduccion = []

posicion_actual = 0
cancion_actual = None
cantidad_canciones = len(cola_reproduccion) + 1
estado = REPRODUCCION