from tkinter import filedialog, messagebox
from os import path, listdir

def escanear_elementos(carpeta):
    elementos_encontrados = listdir(carpeta)
    archivos_filtrados = []
    subcarpetas_encontradas = []

    for elemento in elementos_encontrados:
        ruta_archivo = path.join(carpeta, elemento)

        if path.isdir(ruta_archivo):
            subcarpetas_encontradas.append(ruta_archivo)

        elif ruta_archivo.endswith(".flac") or ruta_archivo.endswith(".mp3"):
            archivos_filtrados.append(ruta_archivo)

    return subcarpetas_encontradas, archivos_filtrados

def escanear_carpeta(carpeta, accion):
    ESCANEAR_SUBCARPETAS = True

    carpetas_encontradas = [carpeta]
    archivos_escaneados = []

    while carpetas_encontradas:
        carpeta_actual = carpetas_encontradas[0]
        subcarpetas, archivos = escanear_elementos(carpeta_actual)

        if accion == ESCANEAR_SUBCARPETAS and subcarpetas:
            carpetas_encontradas.extend(subcarpetas)

        archivos_escaneados.extend(archivos)
        carpetas_encontradas.remove(carpeta_actual)

    return archivos_escaneados

def abrir_carpeta():
    TITULO = "¿Escanear subcarpetas?"
    MENSAJE = "¿Quiere tambien escanear las subcarpetas?"
    CANCELAR = None

    carpeta_abierta = filedialog.askdirectory()
    if not carpeta_abierta:
        return
    
    accion = messagebox.askyesno(title = TITULO, message = MENSAJE)
    if accion == CANCELAR:
        return
    
    nuevas_canciones = escanear_carpeta(carpeta_abierta, accion)
    return nuevas_canciones

abrir_carpeta()