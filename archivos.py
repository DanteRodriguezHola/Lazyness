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

def preguntar_examinar_subcarpetas():
    # === CONFIGURACIONES DE LA VENTANA ===

    titulo_ventana = "¿Examinar subcarpetas?"
    mensaje_ventana = "Se encontro subcarpetas durante la examinación.\n¿Desea examinarlas también?"

    # === CONFIGURACIONES DE LA VENTANA ===
    
    respuesta = messagebox.askyesno(title = titulo_ventana, message = mensaje_ventana)
    
    return respuesta

def examinar_carpetas(carpeta_padre):
    carpetas_restantes = [carpeta_padre]
    canciones_total = []
    accion = False

    ESCANEAR_SUBCARPETAS = True

    while carpetas_restantes:
        carpeta_actual = carpetas_restantes[0]
        canciones, subcarpetas = examinar_elementos(carpeta_actual)

        if carpeta_padre in carpetas_restantes and subcarpetas:
            accion = preguntar_examinar_subcarpetas()

        if accion == ESCANEAR_SUBCARPETAS:
            carpetas_restantes.extend(subcarpetas)

        canciones_total.extend(canciones)
        
        carpetas_restantes.remove(carpeta_actual)

    return canciones_total
        
def abrir_ruta_carpeta():
     # === CONFIGURACIONES DE LA VENTANA ===

    titulo_ventana = "Seleccionar una carpeta"
    carpeta_default = path.expanduser("~/Music")

     # === CONFIGURACIONES DE LA VENTANA ===

    ruta_carpeta = filedialog.askdirectory(title = titulo_ventana, initialdir = carpeta_default)

    if ruta_carpeta:
        canciones = examinar_carpetas(ruta_carpeta)

        return canciones
    
    else:
        return None

# === CARPETAS ===

# === ARCHIVOS ===

def examinar_archivos(ruta_archivos):
    canciones = []

    for ruta_archivo in ruta_archivos:
        if es_audio(ruta_archivo):
            canciones.append(ruta_archivo)

    return canciones

def abrir_rutas_archivos():
    # === CONFIGURACIONES DE LA VENTANA ===

    titulo_ventana = "Seleccionar archivos de audio"
    carpeta_default = path.expanduser("~/Music")
    formatos_audio = [("Archivos de audio", "*.mp3 .flac"), ("Todos los archivos", "*.*")]

    # === CONFIGURACIONES DE LA VENTANA

    rutas_archivos = filedialog.askopenfilenames(title = titulo_ventana, initialdir = carpeta_default, filetypes = formatos_audio)
    
    if rutas_archivos:
        canciones = examinar_archivos(rutas_archivos)

        return canciones
    
    else:
        return None

# === ARCHIVOS ===

# === PLAYLISTS ===

def abrir_ruta_playlist():
    # === CONFIGURACIONES DE LA VENTANA ===

    titulo_ventana = "Seleccionar una playlist"
    carpeta_default = path.expanduser("~/Music")
    formatos_playlist = [("Playlist", "*.m3u .m3u8")]

    # === CONFIGURACIONES DE LA VENTANA ===

    ruta_playlist = filedialog.askopenfilename(title = titulo_ventana, initialdir = carpeta_default, filetypes = formatos_playlist)
    
    return ruta_playlist


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

def leer_playlist():
    ruta_playlist = abrir_ruta_playlist()

    if ruta_playlist:
        canciones = examinar_playlist(ruta_playlist)
        
        return canciones
    
    else:
        return None

def crear_playlist():
    # === CONFIGURACIONES DE LA VENTANA ===

    titulo_ventana = "Crear playlist"
    formato_default = ".m3u8"
    nombre_default = "Mi nueva playlist"
    carpeta_default = path.expanduser("~/Music")
    formatos_playlist = [("MPEG 3.0 URL codificado en UTF-8", "*.m3u8"), ("MPEG 3.0 URL", "*.m3u")]

    # === CONFIGURACIONES DE LA VENTANA ===

    ruta_nueva_playlist = filedialog.asksaveasfilename(title = titulo_ventana, defaultextension = formato_default, initialfile = nombre_default, initialdir = carpeta_default, filetypes = formatos_playlist)

    if ruta_nueva_playlist:
        titulo_playlist = Path(ruta_nueva_playlist).stem

        with open(ruta_nueva_playlist, "w") as playlist:
            playlist.write(f"#EXTINF {titulo_playlist}")

# === PLAYLISTS ===