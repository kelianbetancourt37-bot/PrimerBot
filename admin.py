import random

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
""".strip()

def procesar_adminmenu():
    return mostrar_Adminmenu()

def procesar_ban(user):
    return f"🚫 El usuario {user} ha sido baneado."

def procesar_kick(user):
    return f"🚪 El usuario {user} ha sido expulsado."

def procesar_close():
    return "🔒 El grupo se ha cerrado correctamente."

def procesar_open():
    return "🔓 El grupo se ha abierto correctamente."

def procesar_delete(mensaje_id):
    return f"🗑️ El mensaje con ID {mensaje_id} ha sido eliminado."

def procesar_silenciar(user):
    return f"🔇 El usuario {user} ha sido silenciado."

def procesar_desilenciar(user):
    return f"🔊 El usuario {user} ha sido desilenciado."

def procesar_antilink():
    return "🛡️ El sistema de Antilink ha sido activado en este grupo."

def procesar_antispam():
    return "⚡ El sistema de Antispam ha sido activado."

def procesar_tagall():
    return "📣 ¡Atención a todos los miembros del grupo!"

def procesar_admin_command(command, user=None, mensaje_id=None):
    if command == "ban" and user:
        return procesar_ban(user)
    elif command == "kick" and user:
        return procesar_kick(user)
    elif command == "close":
        return procesar_close()
    elif command == "open":
        return procesar_open()
    elif command == "delete" and mensaje_id:
        return procesar_delete(mensaje_id)
    elif command == "silenciar" and user:
        return procesar_silenciar(user)
    elif command == "desilenciar" and user:
        return procesar_desilenciar(user)
    elif command == "antilink":
        return procesar_antilink()
    elif command == "antispam":
        return procesar_antispam()
    elif command == "tagall":
        return procesar_tagall()
    else:
        return "⚠️ Comando de administración no reconocido o faltan parámetros."
