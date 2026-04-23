REPRODUCCION = False
PAUSA = True

ORDENADO = False
ALEATORIO = True

LINEAL = False
BUCLE = True

cola_base = []
cola_reproduccion = []

posicion_actual = 0
cancion_actual = None

cantidad_canciones = len(cola_reproduccion)
cantidad_indices = len(cola_reproduccion) - 1

estado_reproduccion = REPRODUCCION
tipo_playback = ORDENADO
tipo_repeticion = LINEAL
