from tkinter import filedialog, messagebox
from os import path, listdir
from pathlib import Path
import fleep

import cola

def es_audio(ruta_archivo):
    with open(ruta_archivo, "rb") as archivo:
        tipo_archivo = fleep.get(archivo.read(128))
        if tipo_archivo.type == ["audio"]:
            return True
        
        else:
            return False

# === CARPETAS ===

def examinar_elementos(carpeta):
    elementos_encontrados = listdir(carpeta)

    canciones_encontradas = []
    subcarpetas_encontradas = []

    for elemento in elementos_encontrados:
        ruta_elemento = path.join(carpeta, elemento)

        if path.isdir(ruta_elemento):
            subcarpetas_encontradas.append(ruta_elemento)

        elif es_audio(ruta_elemento):
            canciones_encontradas.append(ruta_elemento)

    return canciones_encontradas, subcarpetas_encontradas

def examinar_carpetas(carpeta_padre):
    carpetas_restantes = [carpeta_padre]
    canciones_total = []

    while carpetas_restantes:
        carpeta_actual = carpetas_restantes[0]
        canciones, subcarpetas = examinar_elementos(carpeta_actual)

        carpetas_restantes.extend(subcarpetas)
        canciones_total.extend(canciones)
        
        carpetas_restantes.remove(carpeta_actual)

    return canciones_total
        
def abrir_ruta_carpeta():
    carpeta = filedialog.askdirectory()
    canciones = examinar_carpetas(carpeta)

    return canciones

# === CARPETAS ===

# === ARCHIVOS ===

def examinar_archivos(ruta_archivos):
    canciones = []

    for ruta_archivo in ruta_archivos:
        if es_audio(ruta_archivo):
            canciones.append(ruta_archivo)

    return canciones

def abrir_rutas_archivos():
    rutas_archivos = filedialog.askopenfilenames()
    canciones = examinar_archivos(rutas_archivos)

    return canciones

# === ARCHIVOS ===

# === PLAYLISTS ===

def examinar_playlist(ruta_playlist):
    canciones = []

    with open(ruta_playlist, "r") as playlist:
        contenido = playlist.readlines()

        for elemento in contenido:
            elemento_limpio = elemento.rstrip("\n")

            if not path.exists(elemento_limpio):
                continue
            
            if not es_audio(elemento_limpio):
                continue

            canciones.append(elemento_limpio)

    return canciones

def abrir_ruta_playlist():
    titulo_ventana = "Seleccione una playlist"
    carpeta_default = "/playlists"
    formatos_playlist = [("Playlist", "*.m3u .m3u8")]
    ruta_playlist = filedialog.askopenfilename(title = titulo_ventana, initialdir = carpeta_default, filetypes = formatos_playlist)
    
    return ruta_playlist

def leer_playlist():
    ruta_playlist = abrir_ruta_playlist()
    canciones = examinar_playlist(ruta_playlist)

    return canciones

def crear_playlist():
    # === DETALLES DE LA VENTANA ===

    titulo_ventana = "Crear playlist"
    formato_default = ".m3u8"
    nombre_default = "Mi nueva playlist"
    carpeta_default = "/playlists"
    formatos_playlist = [("MPEG 3.0 URL codificado en UTF-8", "*.m3u8"), ("MPEG 3.0 URL", "*.m3u")]

    # === DETALLES DE LA VENTANA ===

    ruta_nueva_playlist = filedialog.asksaveasfilename(title = titulo_ventana, defaultextension = formato_default, initialfile = nombre_default, initialdir = carpeta_default, filetypes = formatos_playlist)

    if ruta_nueva_playlist:
        titulo_playlist = Path(ruta_nueva_playlist).stem

        with open(ruta_nueva_playlist, "w") as playlist:
            playlist.write(f"#EXTINF {titulo_playlist}")

abrir_ruta_playlist()
# === PLAYLISTS ===