import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# --- IMPORTACIONES SEGURAS ---
try:
    from menu import mostrar_menu
except ImportError:
    def mostrar_menu(): return "📜 *MENÚ PRINCIPAL*\nUsa .help para ayuda."

try:
    from admin import procesar_adminmenu, procesar_admin_command
except ImportError:
    def procesar_adminmenu(): return "📜 *MENÚ DE ADMINISTRACIÓN*"
    def procesar_admin_command(cmd, user=None, mensaje_id=None): return "⚠️ Error en módulo admin."

try:
    from economia import procesar_trabajar, procesar_diario, procesar_cofre, procesar_depositar, procesar_crimen
except ImportError:
    def procesar_depositar(m, p): return m, f"🏦 Has depositado {p} monedas."
    def procesar_crimen(m): return m + 50, "🥷 Cometiste un crimen exitoso y ganaste 50 monedas."

try:
    # Importar funciones de interacción
    from Interacion import saludar, beso, abrazo, golpe, caricia, eliminar, correr
except ImportError:
    pass

# Variables de estado
monedas_usuario = 500
racha_usuario = 0
coleccion_museo = []

# Argumentos de Node.js
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

    # Economía / Gacha
    elif mensaje_recibido in [".trabajar", ".work", ".w", ".wb"]:
        monedas_usuario, respuesta = procesar_trabajar(monedas_usuario)
        return respuesta

    elif mensaje_recibido in [".daily", ".diario"]:
        monedas_usuario, racha_usuario, respuesta = procesar_diario(monedas_usuario, racha_usuario)
        return respuesta

    elif mensaje_recibido == ".cofre":
        monedas_usuario, racha_usuario, respuesta = procesar_cofre(monedas_usuario, racha_usuario)
        return respuesta

    elif mensaje_recibido in [".depositar", ".dep"]:
        monedas_usuario, respuesta = procesar_depositar(monedas_usuario, parametro)
        return respuesta

    elif mensaje_recibido in [".crimen", ".crime"]:
        monedas_usuario, respuesta = procesar_crimen(monedas_usuario)
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

    else:
        return f"❓ Comando '{mensaje_recibido}' no reconocido. Usa *.menu* para ver la lista."

if __name__ == "__main__":
    try:
        resultado = ejecutar_bot()
        if resultado:
            print(resultado)
    except Exception as error:
        print(f"⚠️ Error al ejecutar el comando en Python: {str(error)}")
