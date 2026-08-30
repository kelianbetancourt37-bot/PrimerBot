def procesar_perfil(datos_usuario):
    nombre = datos_usuario.get("nombre", "Sin registrar")
    genero = datos_usuario.get("genero", "No especificado")
    edad = datos_usuario.get("edad", "Desconocida")
    nacimiento = datos_usuario.get("nacimiento", "No registrada")
    nivel = datos_usuario.get("nivel", 1)
    monedas = datos_usuario.get("monedas", 500)
    banco = datos_usuario.get("banco", 0)
    racha = datos_usuario.get("racha", 0)
    descripcion = datos_usuario.get("descripcion", "Sin biografía.")

    return (
        "╭━━━〔 👤 *TARJETA DE PERFIL* 👤 ━━━╮\n"
        "┃\n"
        f"┃  🏷️ *`Nombre:`* {nombre}\n"
        f"┃  🚻 *`Género:`* {genero}\n"
        f"┃  🎂 *`Edad:`* {edad} años\n"
        f"┃  📅 *`Nacimiento:`* {nacimiento}\n"
        f"┃  📊 *`Nivel:`* Nivel {nivel}\n"
        "┃\n"
        "┣━━ 💰 *ECONOMÍA & RACHA* ━━━\n"
        f"┃  🪙 *`Cartera:`* {monedas} monedas\n"
        f"┃  🏦 *`Banco:`* {banco} monedas\n"
        f"┃  🔥 *`Racha diaria:`* {racha} días\n"
        "┃\n"
        "┣━━ 📝 *BIOGRAFÍA* ━━━\n"
        f"┃  _`{descripcion}`_\n"
        "┃\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━╯\n"
        "_💡 Usa `.setname`, `.setage`, etc., para editar tus datos._"
    )

def procesar_setname(param, datos_usuario, guardar_fn, base_datos):
    if not param:
        return "⚠️ Por favor escribe el nuevo nombre. Ejemplo: `.setname Juan`"
    datos_usuario["nombre"] = param
    guardar_fn(base_datos)
    return f"✅ Nombre actualizado correctamente a: *{param}*"

def procesar_setdesc(param, datos_usuario, guardar_fn, base_datos):
    if not param:
        return "⚠️ Escribe tu nueva biografía."
    datos_usuario["descripcion"] = param
    guardar_fn(base_datos)
    return f"📝 Biografía actualizada correctamente."

def procesar_setage(param, datos_usuario, guardar_fn, base_datos):
    if not param:
        return "⚠️ Especifica tu edad."
    datos_usuario["edad"] = param
    guardar_fn(base_datos)
    return f"🎂 Edad configurada a: *{param}* años."

def procesar_setbirth(param, datos_usuario, guardar_fn, base_datos):
    if not param:
        return "⚠️ Especifica tu fecha de nacimiento."
    datos_usuario["nacimiento"] = param
    guardar_fn(base_datos)
    return f"📅 Fecha de nacimiento guardada: *{param}*."

def procesar_setgene(param, datos_usuario, guardar_fn, base_datos):
    if not param:
        return "⚠️ Especifica tu género. Ejemplo: `.setgene Masculino`"
    datos_usuario["genero"] = param
    guardar_fn(base_datos)
    return f"🚻 Género actualizado a: *{param}*."

def procesar_level(datos_usuario):
    nivel = datos_usuario.get("nivel", 1)
    return f"📊 Tu nivel actual en el bot es: *Nivel {nivel}*."

def procesar_sublevel(param=""):
    return "📈 Progreso de nivel actualizado."

def procesar_levelup(param=""):
    return "🎉 ¡Felicidades! Has subido de nivel."
