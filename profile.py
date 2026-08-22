import random

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

def procesar_level(usuario=""):
    destino = usuario if usuario else "Usted"
    return f"📊 *{destino}* se encuentra en el **Nivel 5** de la vecindad (¡Con experiencia barriendo el patio!)."

def procesar_levelup(usuario=""):
    destino = usuario if usuario else "Vecino"
    return f"🎉 ¡Felicidades {destino}! Ha ascendido al **Nivel 6** de la vecindad. ¡Se ganó una torta de jamón! 🥪🚀"
