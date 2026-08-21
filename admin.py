import random


def procesar_ban(user):
    # Lógica para procesar el comando de ban
    return f"Usuario {user} ha sido baneado del servidor."

def procesar_kick(user):
    # Lógica para procesar el comando de kick
    return f"Usuario {user} ha sido expulsado del servidor."

def procesar_close():
    # Lógica para procesar el comando de close
    return "El bot se ha cerrado correctamente."

def procesar_open():
    # Lógica para procesar el comando de open
    return "El bot se ha abierto correctamente."

def procesar_delete(mensaje_id):
    # Lógica para procesar el comando de delete
    return f"Mensaje con ID {mensaje_id} ha sido eliminado."

def procesar_silenciar(user):
    # Lógica para procesar el comando de silenciar
    return f"Usuario {user} ha sido silenciado en el servidor."

def procesar_desilenciar(user):
    # Lógica para procesar el comando de desilenciar
    return f"Usuario {user} ha sido desilenciado en el servidor."

def procesar_antilink():
    # Lógica para procesar el comando de antilink
    return f"As sido expulsado del servidor por enviar links, si crees que esto es un error contacta con un administrador."
    return "El sistema de antilink ha sido activado."

def procesar_antispam():
    # Lógica para procesar el comando de antispam
    return "El sistema de antispam ha sido activado."

def procesar_tagall():
    # Lógica para procesar el comando de tagall
    return "Todos los miembros del grupo han sido mencionados."

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
        return "Comando de administración no reconocido o faltan parámetros."