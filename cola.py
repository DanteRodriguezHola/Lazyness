REPRODUCCION = False
PAUSA = True

NORMAL = False
ALEATORIO = True

cola_base = []
cola_reproduccion = []

posicion_actual = 0
cancion_actual = None
cantidad_canciones = len(cola_reproduccion) - 1

estado = REPRODUCCION
playback = NORMAL
bucle = True