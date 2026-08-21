import random

def procesar_Medifire(link):
    if "mediafire.com" in link:
        mensaje = f"🔗 Descarga desde Mediafire: {link}"
    else:
        mensaje = "❌ El enlace proporcionado no es de Mediafire."
    return mensaje

def procesar_Mega(link):
    if "mega.nz" in link:
        mensaje = f"🔗 Descarga desde Mega: {link}"
    else:
        mensaje = "❌ El enlace proporcionado no es de Mega."
    return mensaje

def procesar_descargar(link):
    if "mediafire.com" in link:
        return procesar_Medifire(link)
    elif "mega.nz" in link:
        return procesar_Mega(link)
    else:
        return "❌ El enlace proporcionado no es válido para descargar."

def descargar_facebook(link):
    if "facebook.com" in link:
        mensaje = f"🔗 Descarga desde Facebook: {link}"
    else:
        mensaje = "❌ El enlace proporcionado no es de Facebook."
    return mensaje

def descargar_instagram(link):
    if "instagram.com" in link:
        mensaje = f"🔗 Descarga desde Instagram: {link}"
    else:
        mensaje = "❌ El enlace proporcionado no es de Instagram."
    return mensaje

def descargar_tiktok(link):
    if "tiktok.com" in link:
        mensaje = f"🔗 Descarga desde TikTok: {link}"
    else:
        mensaje = "❌ El enlace proporcionado no es de TikTok."
    return mensaje

def descargar_youtube(link):
    if "youtube.com" in link or "youtu.be" in link:
        mensaje = f"🔗 Descarga desde YouTube: {link}"
    else:
        mensaje = "❌ El enlace proporcionado no es de YouTube."
    return mensaje

def procesar_mp3(link):
    if "youtube.com" in link or "youtu.be" in link:
        mensaje = f"🎵 Descarga de MP3 desde YouTube: {link}"
    else:
        mensaje = "❌ El enlace proporcionado no es válido para descargar MP3."
    return mensaje

def procesar_mp4(link):
    if "youtube.com" in link or "youtu.be" in link:
        mensaje = f"🎥 Descarga de MP4 desde YouTube: {link}"
    else:
        mensaje = "❌ El enlace proporcionado no es válido para descargar MP4."
    return mensaje

def procesar_imagenes(buscar):
    if buscar:
        mensaje = f"buscando imagenes relacionadascon: *{buscar}*...\n"
    else:
        mensaje = "por favor, proporciona un término de búsqueda. Ejemplo: `.imagen gatos`"
        return mensaje

def procesar_sticker(url):
    if url and (url.endswith(".webp") or url.endswith(".png") or url.endswith(".webp")):
        mensaje = f"🖼 Descarga de sticker desde URL: {url}"
    else:
        mensaje = "❌ El enlace proporcionado no es de sticker."
    return mensaje

def procesar_pinterest(buscar):
    if buscar:
        mensaje = f"buscando en pinterest: *{buscar}*...\n"
    else:
        mensaje = "por favor, proporciona un termino de búsqueda. Ejemplo. `.pin perros`"
        return mensaje