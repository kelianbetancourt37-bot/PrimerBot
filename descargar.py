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
        # Aquí puedes agregar una URL de prueba o lógica de imagen si deseas que el bot mande una foto real
        return f"🖼️ Buscando imágenes relacionadas con: *{buscar}*..."
    else:
        return "❌ Por favor, proporciona un término de búsqueda. Ejemplo: `.imagen gatos`"

def procesar_sticker(url):
    if url and (url.endswith(".webp") or url.endswith(".png") or url.endswith(".jpg") or url.endswith(".jpeg")):
        mensaje = f"🖼️ Descarga de sticker desde URL: {url}"
    else:
        mensaje = "❌ El enlace proporcionado no es válido para un sticker (debe ser .png, .jpg o .webp)."
    return mensaje

def procesar_pinterest(buscar):
    if buscar:
        # Retorna el texto junto con el link de la imagen para que WhatsApp la muestre como miniatura
        return f"📌 Pinterest: Resultados para *{buscar}*:\nhttps://images.unsplash.com/photo-1514888286974-6c03e2ca1dba"
    else:
        return "❌ Por favor, proporciona un término de búsqueda. Ejemplo: `.pin gatos`"
