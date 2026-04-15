import pygame
import os

from abrir_carpeta import abrir_carpeta

pygame.mixer.init()

cola_base = []
cola_reproduccion = []

posicion_actual = 0
cancion_actual = None

REPRODUCCION = False
PAUSA = True

estado = REPRODUCCION

def mostrar_controles():
    os.system("cls")

    print("[<] --> Anterior canción")
    print("[/] --> Pausar / Reanudar")
    print("[O] --> Stop")
    print("[>] --> Siguente canción")
    print("")

def controles():
    global estado
    ingreso = input("Ingrese --> ")
    
    match ingreso:
        case "/":
            if estado == PAUSA:
                pygame.mixer.music.unpause()

            elif estado == REPRODUCCION:
                pygame.mixer.music.pause()

            estado = not(estado)

        case "<":
            

def actualizar_cancion():
    if cola_reproduccion:
        cancion_actual = cola_reproduccion[posicion_actual]

    else:
        cancion_actual = None

    return cancion_actual

cola_reproduccion.extend(abrir_carpeta())

print(cola_reproduccion)

cancion_actual = actualizar_cancion()

while cola_reproduccion:
    pygame.mixer.music.load(cancion_actual)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() or estado == PAUSA:
        mostrar_controles()
        controles()

