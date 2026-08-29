import random

def procesar_perfil(usuario=""):
    destino = usuario if usuario else "Vecino"
    
    apodos = ["El Chavo del Ocho", "La Chilindrina", "Don Ramón", "Kiko", "Doña Florinda", "El Profesor Jirafales", "El Señor Barriga", "La Bruja del 71"]
    apodo_aleatorio = random.choice(apodos)
    
    mensaje =(
        "╭━━━〔 👤 *TARJETA DE PERFIL* 👤 ━━━╮\n"
        "┃\n"
        f"┃  🏷️ *Nombre:* {nombre}\n"
        f"┃  🚻 *Género:* {genero}\n"
        f"┃  🎂 *Edad:* {edad} años\n"
        f"┃  📅 *Nacimiento:* {nacimiento}\n"
        f"┃  📊 *Nivel:* Nivel {nivel}\n"
        "┃\n"
        "┣━━ 💰 *ECONOMÍA & RACHA* ━━━\n"
        f"┃  🪙 *Cartera:* {monedas} monedas\n"
        f"┃  🏦 *Banco:* {banco} monedas\n"
        f"┃  🔥 *Racha diaria:* {racha} días\n"
        "┃\n"
        "┣━━ 📝 *BIOGRAFÍA* ━━━\n"
        f"┃  _{descripcion}_\n"
        "┃\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯\n"
        "_💡 Usa `.setname`, `.setage`, etc., para editar tus datos._"
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
