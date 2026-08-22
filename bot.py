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
    from economia import procesar_trabajar, procesar_diario, procesar_cofre, procesar_depositar, procesar_crimen, procesar_banco
except ImportError:
    def procesar_depositar(m, b, p): return m, b, f"🏦 Has depositado {p} monedas."
    def procesar_crimen(m): return m + 50, "🥷 Cometiste un crimen exitoso y ganaste 50 monedas."
    def procesar_banco(m, b): return m, b, f"🏦 Dinero en mano: {m} | Banco: {b}"

try:
    from Interacion import saludar, beso, abrazo, golpe, caricia, eliminar, correr
except ImportError:
    pass

try:
    from perfil import procesar_perfil, procesar_setname, procesar_setdesc, procesar_setage, procesar_setbirth, procesar_setgene, procesar_level, procesar_levelup
except ImportError:
    def procesar_perfil(u=""): return f"👤 Perfil de {u or 'Usuario'}"
    def procesar_setname(p=""): return f"✅ Nombre actualizado a: {p}"
    def procesar_setdesc(p=""): return f"📝 Descripción actualizada."
    def procesar_setage(p=""): return f"🎂 Edad configurada a: {p}"
    def procesar_setbirth(p=""): return f"📅 Nacimiento guardado: {p}"
    def procesar_setgene(p=""): return f"🚻 Género actualizado: {p}"
    def procesar_level(u=""): return f"📊 Nivel del usuario."
    def procesar_levelup(u=""): return f"🎉 ¡Subiste de nivel!"

# Importación de las funciones de descarga que creaste
try:
    from descargas import (procesar_descargar, descargar_facebook, descargar_instagram, 
                           descargar_tiktok, descargar_youtube, procesar_mp3, 
                           procesar_mp4, procesar_imagenes, procesar_sticker, procesar_pinterest)
except ImportError:
    def procesar_descargar(l): return f"🔗 Descarga: {l}"
    def descargar_facebook(l): return f"🔗 FB: {l}"
    def descargar_instagram(l): return f"🔗 IG: {l}"
    def descargar_tiktok(l): return f"🔗 TT: {l}"
    def descargar_youtube(l): return f"🔗 YT: {l}"
    def procesar_mp3(l): return f"🎵 MP3: {l}"
    def procesar_mp4(l): return f"🎥 MP4: {l}"
    def procesar_imagenes(b): return f"🖼️ Imágenes: {b}"
    def procesar_sticker(u): return f"🖼️ Sticker: {u}"
    def procesar_pinterest(b): return f"📌 Pinterest: {b}"

# Variables de estado
monedas_usuario = 500
banco_usuario = 0
racha_usuario = 0
coleccion_museo = []

# Argumentos de Node.js
args = sys.argv[1:]
mensaje_recibido = args[0].lower().strip() if len(args) > 0 else ".menu"
parametro = args[1].strip() if (len(args) > 1 and args[1] != "None") else ""

def ejecutar_bot():
    global monedas_usuario, banco_usuario, racha_usuario, coleccion_museo

    # Menú Principal
    if mensaje_recibido in [".menu", ".help"]:
        return mostrar_menu()

    elif mensaje_recibido == ".adminmenu":
        return procesar_adminmenu()

    # Economía / Gacha
    elif mensaje_recibido in [".crimen", ".crime"]:
        monedas_usuario, respuesta = procesar_crimen(monedas_usuario)
        return respuesta

    elif mensaje_recibido in [".trabajar", ".work", ".w", ".wb"]:
        monedas_usuario, respuesta = procesar_trabajar(monedas_usuario)
        return respuesta

    elif mensaje_recibido in [".cofre", ".daily"]:
        monedas_usuario, racha_usuario, respuesta = procesar_cofre(monedas_usuario, racha_usuario)
        return respuesta

    elif mensaje_recibido in [".banco", ".bank"]:
        monedas_usuario, banco_usuario, respuesta = procesar_banco(monedas_usuario, banco_usuario)
        return respuesta

    elif mensaje_recibido in [".banco", ".bank"]:
        monedas_usuario, banco_usuario, respuesta = procesar_banco(monedas_usuario, banco_usuario)
        return respuesta

    # Comandos de Perfil y Usuario
    elif mensaje_recibido == ".perfil":
        return procesar_perfil(parametro)

    elif mensaje_recibido == ".setname":
        return procesar_setname(parametro)

    elif mensaje_recibido == ".setdesc":
        return procesar_setdesc(parametro)

    elif mensaje_recibido == ".setage":
        return procesar_setage(parametro)

    elif mensaje_recibido == ".setbirth":
        return procesar_setbirth(parametro)

    elif mensaje_recibido == ".setgene":
        return procesar_setgene(parametro)

    elif mensaje_recibido == ".level":
        return procesar_level(parametro)

    elif mensaje_recibido == ".levelup":
        return procesar_levelup(parametro)

    # Comandos de Descarga
    elif mensaje_recibido in [".mediafire", ".mega", ".descargar"]:
        return procesar_descargar(parametro)

    elif mensaje_recibido == ".fb":
        return descargar_facebook(parametro)

    elif mensaje_recibido == ".ig":
        return descargar_instagram(parametro)

    elif mensaje_recibido == ".tt":
        return descargar_tiktok(parametro)

    elif mensaje_recibido == ".yt":
        return descargar_youtube(parametro)

    elif mensaje_recibido == ".mp3":
        return procesar_mp3(parametro)

    elif mensaje_recibido == ".mp4":
        return procesar_mp4(parametro)

    elif mensaje_recibido == ".imagen":
        return procesar_imagenes(parametro)

    elif mensaje_recibido == ".sticker":
        return procesar_sticker(parametro)

    elif mensaje_recibido == ".pin":
        return procesar_pinterest(parametro)

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
