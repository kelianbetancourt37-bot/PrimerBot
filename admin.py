import random, os

def mostrar_Adminmenu():
    return """
👑 *MENÚ DE ADMINISTRADORES* 👑

📌 *.ban* @usuario - Banear a un usuario
📌 *.kick* @usuario - Expulsar del grupo
📌 *.close* - Cerrar el grupo
📌 *.open* - Abrir el grupo
📌 *.silenciar* @usuario - Silenciar usuario
📌 *.desilenciar* @usuario - Desilenciar usuario
📌 *.antilink* - Activar/Desactivar Antilink
📌 *.antispam* - Activar/Desactivar Antispam
📌 *.tagall* - Mencionar a todos
📌 *.delete* [ID] - Eliminar un mensaje
📌 *.boton* - Encender el bot
📌 *.botoff* - Apagar el bot
""".strip()

def procesar_adminmenu():
    return mostrar_Adminmenu()

def procesar_ban(user, base_datos, guardar_fn):
    if user in base_datos:
        base_datos.pop(user)
        guardar_fn(base_datos)
        return f"✅ Usuario {user} baneado."
    else:
        return f"❌ Usuario {user} no encontrado."

def procesar_kick(user, base_datos, guardar_fn):
    if user in base_datos:
        base_datos.pop(user)
        guardar_fn(base_datos)
        return f"✅ Usuario {user} expulsado."
    else:
        return f"❌ Usuario {user} no encontrado."

def procesar_close():
    return "✅ Grupo cerrado."

def procesar_open():
    return "✅ Grupo abierto."

def procesar_antilink():
    return "✅ Antilink activado."

def procesar_antispam():
    return "✅ Antispam activado."

def procesar_tagall():
    return (
        "📢 *¡ATENCIÓN A TODOS LOS MIEMBROS!* 📢\n\n"
        "╭━━━〔 👥 *MENCIÓN GENERAL* 👥 ━━━╮\n"
        "┃\n"
        "┃  💬 _Se requiere la presencia_ \n"
        "┃  _de todos en el grupo._\n"
        "┃\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯"
    )

def procesar_delete(mensaje_id):
    if mensaje_id:
        return f"🗑️ Mensaje con ID `{mensaje_id}` eliminado."
    else:
        return "⚠️ Por favor responde al mensaje que deseas eliminar con `.delete`."
        
def procesar_bot_off():
    return "✅ Bot apagado correctamente. (Usa .boton para encenderlo)"

def procesar_bot_on():
    return "✅ ¡Bot encendido de nuevo!"

def procesar_admin_command(cmd, user=None, mensaje_id=None, base_datos=None, guardar_fn=None):
    if cmd == "ban":
        return procesar_ban(user, base_datos, guardar_fn)
    elif cmd == "kick":
        return procesar_kick(user, base_datos, guardar_fn)
    elif cmd == "close":
        return procesar_close()
    elif cmd == "open":
        return procesar_open()
    elif cmd == "antilink":
        return procesar_antilink()
    elif cmd == "antispam":
        return procesar_antispam()
    elif cmd == "tagall":
        return procesar_tagall()
    elif cmd == "delete":
        return procesar_delete(mensaje_id)
    elif cmd == "boton":
        return procesar_bot_on()
    elif cmd == "botoff":    
        return procesar_bot_off()
    else:
        return "⚠️ Error en módulo admin."
