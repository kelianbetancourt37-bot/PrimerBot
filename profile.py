import random

def procesar_perfil(usuario_id, datos_usuario):
    nombre = datos_usuario.get("nombre", "Sin registrar")
    genero = datos_usuario.get("genero", "No especificado")
    edad = datos_usuario.get("edad", "Desconocida")
    nacimiento = datos_usuario.get("nacimiento", "No registrada")
    descripcion = datos_usuario.get("descripcion", "Sin biografía.")
    nivel = datos_usuario.get("nivel", 1)
    monedas = datos_usuario.get("monedas", 500)
    banco = datos_usuario.get("banco", 0)
    racha = datos_usuario.get("racha", 0)

    return (
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

def procesar_setname(nuevo_nombre=""):
    if not nuevo_nombre:
        return "⚠️ Vecino, ¿cómo se va a llamar? Escriba bien. Ejemplo: .setname Don Ramón"
    return f"✅ ¡Vaya! Su nuevo nombre en la vecindad es: *{nuevo_nombre}*"

def procesar_setdesc(nueva_desc=""):
    if not nueva_desc:
        return "⚠️ Escriba su descripción o chisme de la vecindad. Ejemplo: .setdesc Vendiendo churros"
    return f"📝 Su recado o descripción quedó registrado en la pared de la vecindad:\n_{nueva_desc}_"

def procesar_setage(edad=""):
    if not edad.isdigit():
        return "⚠️ Ponga una edad en números, no invente. Ejemplo: .setage 30"
    return f"🎂 Con que tiene *{edad} años*... ¡Ya está grande para andar jugando con la resortera!"

def procesar_setbirth(fecha=""):
    if not fecha:
        return "⚠️ Indique su fecha de nacimiento. Ejemplo: .setbirth 01/01/2000"
    return f"📅 Fecha anotada en el calendario de la vecindad: *{fecha}*"

def procesar_setgene(genero=""):
    if not genero:
        return "⚠️ Especifique su género. Ejemplo: .setgene Masculino"
    return f"🚻 Género registrado correctamente: *{genero}*"

def procesar_sublevel(usuario=""):
    destino = usuario if usuario else "Usted"
    return f"🆙 ¡{destino} sube su nivel! ¡Ahora está en el **Nivel 6** de la vecindad!"

def procesar_level(usuario=""):
    destino = usuario if usuario else "Usted"
    return f"📊 *{destino}* se encuentra en el **Nivel 5** de la vecindad (¡Con experiencia barriendo el patio!)."

def procesar_levelup(usuario=""):
    destino = usuario if usuario else "Vecino"
    return f"🎉 ¡Felicidades {destino}! Ha ascendido al **Nivel 6** de la vecindad. ¡Se ganó una torta de jamón! 🥪🚀"
