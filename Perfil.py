def procesar_perfil(datos_usuario):
    nombre = datos_usuario.get("nombre", "Sin nombre")
    genero = datos_usuario.get("genero", "No especificado")
    edad = datos_usuario.get("edad", "No especificada")
    nacimiento = datos_usuario.get("nacimiento", "No especificado")
    nivel = datos_usuario.get("nivel", 1)
    nivel_progreso = datos_usuario.get("nivel_progreso", "[░░░░░░░░░░] 0%")
    monedas = datos_usuario.get("monedas", 500)
    banco = datos_usuario.get("banco", 0)
    racha = datos_usuario.get("racha", 0)
    descripcion = datos_usuario.get("descripcion", "Sin biografía.")

    return (
        f"╭─ 👤 *TARJETA DE PERFIL* 👤 ─╮\n"
        f"│\n"
        f"│  🏷️ *Nombre:* {nombre}\n"
        f"│  🚻 *Género:* {genero}\n"
        f"│  🎂 *Edad:* {edad} años\n"
        f"│  📅 *Nacimiento:* {nacimiento}\n\n"
        f"│  ⭐ *Nivel:* Nivel {nivel}\n"
        f"│  📈 *Progreso de nivel:* {nivel_progreso}\n"
        f"│\n"
        f"├─ 💰 *ECONOMÍA & RACHA* ─┤\n"
        f"│  💵 *Cartera:* {monedas} monedas\n"
        f"│  🏦 *Banco:* {banco} monedas\n"
        f"│  🔥 *Racha diaria:* {racha} días\n"
        f"│\n"
        f"├─ 📝 *BIOGRAFÍA* ─┤\n"
        f"│  _{descripcion}_\n"
        f"│\n"
        f"╰──────────────────────────╯\n"
        f"💡 _Usa `.setname`, `.setage`, etc., para editar tus datos._"
    )
