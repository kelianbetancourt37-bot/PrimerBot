import sys
import os

# Forzar salida en UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Importaciones seguras con Try/Except individual
try:
    from menu import mostrar_menu
except ImportError:
    def mostrar_menu(): return "📜 *MENÚ PRINCIPAL*\nUsa .help para ayuda."

try:
    # Intenta importar desde Adminmenu.py o admin.py según el nombre que tengas
    try:
        from Adminmenu import mostrar_Adminmenu as procesar_adminmenu
    except ImportError:
        from admin import procesar_adminmenu
except ImportError:
    def procesar_adminmenu(): return "📜 *MENÚ DE ADMINISTRACIÓN*\nUsa .help para ayuda."

try:
    from economia import procesar_trabajar, procesar_diario, procesar_cofre
except ImportError:
    pass

try:
    from museo import obtener_museo, comprar_reliquia
except ImportError:
    pass

try:
    from admin import procesar_admin_command
except ImportError:
    pass

try:
    from Interacion import *
except ImportError:
    pass

try:
    from gestion import activar_desactivar_bienvenida, mostrar_reglas
except ImportError:
    pass

try:
    from descargar import *
except ImportError:
    pass

# Variables de prueba
monedas_usuario = 500
racha_usuario = 0
coleccion_museo = []

# Lee los argumentos enviados desde Node.js
args = sys.argv[1:]
mensaje_recibido = args[0].lower().strip() if len(args) > 0 else ".menu"
parametro = args[1].strip() if (len(args) > 1 and args[1] != "None") else ""

def ejecutar_bot():
    global monedas_usuario, racha_usuario, coleccion_museo

    # Menú Principal
    if mensaje_recibido in [".menu", ".help"]:
        return mostrar_menu()

    elif mensaje_recibido == ".adminmenu":
        return procesar_adminmenu()

    # Economía
    elif mensaje_recibido in [".trabajar", ".work", ".w", ".wb"]:
        monedas_usuario, respuesta = procesar_trabajar(monedas_usuario)
        return respuesta

    elif mensaje_recibido in [".daily", ".diario"]:
        monedas_usuario, racha_usuario, respuesta = procesar_diario(monedas_usuario, racha_usuario)
        return respuesta

    elif mensaje_recibido == ".cofre":
        monedas_usuario, racha_usuario, respuesta = procesar_cofre(monedas_usuario, racha_usuario)
        return respuesta

    elif mensaje_recibido == ".museo":
        return obtener_museo(coleccion_museo)

    elif mensaje_recibido == ".comprarmuseo":
        monedas_usuario, coleccion_museo, respuesta = comprar_reliquia(monedas_usuario, coleccion_museo)
        return respuesta

    # Comandos de Administración
    elif mensaje_recibido in [".ban", ".kick", ".silenciar", ".desilenciar"]:
        comando_limpio = mensaje_recibido.replace(".", "")
        return procesar_admin_command(comando_limpio, user=parametro)

    elif mensaje_recibido in [".close", ".open", ".antilink", ".antispam", ".tagall"]:
        comando_limpio = mensaje_recibido.replace(".", "")
        return procesar_admin_command(comando_limpio)

    elif mensaje_recibido == ".delete":
        return procesar_admin_command("delete", mensaje_id=parametro)

    # Interacción
    elif mensaje_recibido == ".saludar":
        return saludar(parametro)

    elif mensaje_recibido == ".beso":
        return beso(parametro)

    elif mensaje_recibido == ".abrazo":
        return abrazo(parametro)

    elif mensaje_recibido == ".golpe":
        return golpe(parametro)

    elif mensaje_recibido == ".kill":
        return eliminar(parametro)

    elif mensaje_recibido == ".caricia":
        return caricia(parametro)

    elif mensaje_recibido == ".correr":
        return correr(parametro)

    # Gestión de Grupos
    elif mensaje_recibido == ".welcome":
        return activar_desactivar_bienvenida(parametro)

    elif mensaje_recibido == ".reglas":
        return mostrar_reglas()

    # Descargas de medios
    elif mensaje_recibido == ".mediafire":
        return descargar_mediafire(parametro)

    elif mensaje_recibido == ".mega":
        return descargar_mega(parametro)

    elif mensaje_recibido == ".descargar":
        return descargar(parametro)

    elif mensaje_recibido == ".facebook":
        return descargar_facebook(parametro)

    elif mensaje_recibido == ".instagram":
        return descargar_instagram(parametro)

    elif mensaje_recibido == ".tiktok":
        return descargar_tiktok(parametro)

    elif mensaje_recibido == ".youtube":
        return descargar_youtube(parametro)

    elif mensaje_recibido == ".mp3":
        return procesar_mp3(parametro)

    elif mensaje_recibido == ".mp4":
        return procesar_mp4(parametro)

    elif mensaje_recibido == ".imagen":
        return procesar_imagenes(parametro)

    elif mensaje_recibido == ".sticker":
        return procesar_sticker(parametro)

    else:
        return f"❓ Comando '{mensaje_recibido}' no reconocido. Usa *.menu* para ver la lista de comandos disponibles."

if __name__ == "__main__":
    try:
        resultado = ejecutar_bot()
        if resultado:
            print(resultado)
    except Exception as error:
        print(f"⚠️ Error al ejecutar el comando en Python: {str(error)}")
