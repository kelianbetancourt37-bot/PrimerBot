import random.choice


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
