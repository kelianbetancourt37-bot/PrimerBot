import random

def procesar_perfil(usuario=""):
    destino = usuario if usuario else "Vecino"
    
    apodos = ["El Chavo del Ocho", "La Chilindrina", "Don Ramón", "Kiko", "Doña Florinda", "El Profesor Jirafales", "El Señor Barriga", "La Bruja del 71"]
    apodo_aleatorio = random.choice(apodos)
    
    mensaje = (
        f"🏘️ *LA VECINDAD DEL BOT* 🏠\n\n"
        f"👤 *Inquilino:* *{destino}*\n"
        f"🏷️ *Apodo en la vecindad:* _{apodo_aleatorio}_\n"
        f"🏠 *Vivienda:* Casa número {random.randint(1, 74)}\n"
        f"📝 *Frase célebre:* \"¡Eso, eso, eso!\" o \"¡No te doy otra patada porque...\"\n"
        f"🎂 *Edad:* {random.randint(8, 60)} años (¡crujiendo los huesos!)\n"
        f"💰 *Deuda de la renta:* ${random.randint(0, 14)} meses con el Señor Barriga 💸\n"
        f"📊 *Nivel en la vecindad:* *Nivel 5* (Vecino honorable)"
    )
    return mensaje

def procesar_setname(param=""):
    return f"✅ Nombre actualizado correctamente a: *{param}*" if param else "⚠️ Por favor escribe el nuevo nombre. Ejemplo: `.setname Juan`"

def procesar_setdesc(param=""):
    return f"📝 Descripción actualizada correctamente." if param else "⚠️ Escribe tu nueva biografía."

def procesar_setage(param=""):
    return f"🎂 Edad configurada a: *{param}* años." if param else "⚠️ Especifica tu edad."

def procesar_setbirth(param=""):
    return f"📅 Fecha de nacimiento guardada: *{param}*." if param else "⚠️ Especifica tu fecha de nacimiento."

def procesar_setgene(param=""):
    return f"🚻 Género actualizado a: *{param}*." if param else "⚠️ Especifica tu género."

def procesar_level(param=""):
    return "📊 Tu nivel actual en el bot es: *Nivel 5*."

def procesar_sublevel(param=""):
    return "📈 Progreso de nivel actualizado."

def procesar_levelup(param=""):
    return "🎉 ¡Felicidades! Has subido de nivel."
