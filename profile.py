import random

def procesar_perfil(usuario=""):
    destino = usuario if usuario else "Usuario"
    opciones = [
        f"👤 *Perfil de {destino}*\n✨ Nivel: 5\n⭐ Experiencia: 450/1000\n💼 Estado: Activo",
        f"👤 *Perfil de {destino}*\n🛡️ Nivel: 12\n⭐ Experiencia: 1200/2000\n💼 Estado: Legendario"
    ]
    return random.choice(opciones)

def procesar_setname(nuevo_nombre=""):
    if not nuevo_nombre:
        return "⚠️ Debes escribir un nuevo nombre. Ejemplo: .setname Juan"
    return f"✅ El nombre ha sido actualizado correctamente a: *{nuevo_nombre}*"

def procesar_setdesc(nueva_desc=""):
    if not nueva_desc:
        return "⚠️ Debes escribir una descripción. Ejemplo: .setdesc Hola a todos"
    return f"📝 Descripción actualizada con éxito:\n_{nueva_desc}_"

def procesar_setage(edad=""):
    if not edad.isdigit():
        return "⚠️ Por favor, ingresa una edad válida en números. Ejemplo: .setage 18"
    return f"🎂 Tu edad ha sido configurada a: *{edad} años*"

def procesar_setbirth(fecha=""):
    if not fecha:
        return "⚠️ Especifica tu fecha de nacimiento. Ejemplo: .setbirth 01/01/2000"
    return f"📅 Fecha de nacimiento guardada: *{fecha}*"

def procesar_setgene(genero=""):
    if not genero:
        return "⚠️ Especifica tu género. Ejemplo: .setgene Masculino"
    return f"🚻 Género actualizado a: *{genero}*"

def procesar_level(usuario=""):
    destino = usuario if usuario else "Tu"
    return f"📊 *{destino}* se encuentra en el **Nivel 5** (Experiencia: 450/1000)."

def procesar_levelup(usuario=""):
    destino = usuario if usuario else "Usuario"
    return f"🎉 ¡Felicidades {destino}! Has subido al **Nivel 6** con éxito. 🚀"