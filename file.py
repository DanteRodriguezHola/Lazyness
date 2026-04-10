from tkinter import filedialog, messagebox

import os

def escanear_archivos(carpeta):
    archivos_escaneados = os.listdir(carpeta)
    archivos_filtrados = []
    carpetas_encontradas = []

    for archivo in archivos_escaneados:
        ruta_archivo = os.path.join(carpeta, archivo)

        if os.path.isdir(ruta_archivo):
            carpetas_encontradas.append(ruta_archivo)

        elif archivo.endswith(".mp3") or archivo.endswith(".flac"):
            archivos_filtrados.append(ruta_archivo)

    return carpetas_encontradas, archivos_filtrados

def escanear_carpetas(carpeta):
    carpetas_restantes = [carpeta]
    archivos_encontrados = []

    while carpetas_restantes:
        carpeta_actual = carpetas_restantes[0]
        carpetas_encontradas, archivos_filtrados = escanear_archivos(carpeta_actual)

        if carpetas_encontradas:
            carpetas_restantes.extend(carpetas_encontradas)
        
        archivos_encontrados.extend(archivos_filtrados)
        carpetas_restantes.remove(carpeta_actual)

    return archivos_encontrados

def abrir_carpeta():
    carpeta = filedialog.askdirectory()
    escanear_subcarpetas = messagebox.askyesnocancel()
    archivos = escanear_carpetas(carpeta)

    for archivo in archivos:
        print(archivo)

    return archivos

abrir_carpeta()