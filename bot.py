import sys
import os
import json

sys.stdout.reconfigure(encoding='utf-8')

# --- CONFIGURACIÓN DE BASE DE DATOS JSON ---
DB_FILE = "usuarios.json"

def cargar_todos_los_datos():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return {}

def guardar_todos_los_datos(datos):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)

# Cargamos toda la base de datos de usuarios
base_datos = cargar_todos_los_datos()

# Argumentos de Node.js
args = sys.argv[1:]
mensaje_recibido = args[0].lower().strip() if len(args) > 0 else ".menu"
parametro = args[1].strip() if (len(args) > 1 and args[1] != "None") else ""
usuario_id = args[2].strip() if (len(args) > 2 and args[2] != "None") else "usuario_general"

# Registrar usuario si es nuevo con todos sus campos de tiempo
if usuario_id not in base_datos:
    base_datos[usuario_id] = {
        "monedas": 500,
        "banco": 0,
        "racha": 0,
        "ultimo_trabajo": 0,
        "ultimo_diario": 0,
        "ultimo_cofre": 0,
        "ultimo_crimen": 0
    }
    guardar_todos_los_datos(base_datos)

datos_usuario = base_datos[usuario_id]
monedas_usuario = datos_usuario.get("monedas", 500)
banco_usuario = datos_usuario.get("banco", 0)
racha_usuario = datos_usuario.get("racha", 0)
ultimo_trabajo = datos_usuario.get("ultimo_trabajo", 0)
ultimo_diario = datos_usuario.get("ultimo_diario", 0)
ultimo_cofre = datos_usuario.get("ultimo_cofre", 0)
ultimo_crimen = datos_usuario.get("ultimo_crimen", 0)
coleccion_museo = []

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
    from Interacion import saludar, beso, abrazo, golpe, caricia, eliminar, correr
except ImportError:
    def saludar(u=""): return f"👋 Saludos a {u or 'alguien'}."
    def beso(u=""): return f"💋 Beso para {u or 'alguien'}."
    def abrazo(u=""): return f"🤗 Abrazo para {u or 'alguien'}."
    def golpe(u=""): return f"🥊 Golpe para {u or 'alguien'}."
    def caricia(u=""): return f"🫂 Caricia para {u or 'alguien'}."
    def eliminar(u=""): return f"💥 Eliminado."
    def correr(u=""): return f"🏃 Corriendo..."

try:
    from Perfil import procesar_perfil, procesar_setname, procesar_setdesc, procesar_setage, procesar_setbirth, procesar_setgene, procesar_level, procesar_levelup
except ImportError:
    def procesar_perfil(u=""): return f"👤 Perfil de {u or 'Usuario'}"
    def procesar_setname(p=""): return f"✅ Nombre actualizado a: {p}"
    def procesar_setdesc(p=""): return f"📝 Descripción actualizada."
    def procesar_setage(p=""): return f"🎂 Edad configurada a: {p}"
    def procesar_setbirth(p=""): return f"📅 Nacimiento guardado: {p}"
    def procesar_setgene(p=""): return f"🚻 Género actualizado: {p}"
    def procesar_level(u=""): return f"📊 Nivel del usuario."
    def procesar_levelup(u=""): return f"🎉 ¡Subiste de nivel!"

# Importación de las funciones de descarga y economía
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

try:
    from economia import (procesar_trabajar, procesar_diario, procesar_cofre, 
                          procesar_crimen, procesar_depositar, procesar_retirar, 
                          procesar_banco, procesar_Mercado, procesar_comprar_pokeballs)
except ImportError:
    def procesar_trabajar(u, m, t): return m, t, "⚠️ Módulo de economía no disponible."
    def procesar_diario(u, m, r, t): return m, r, t, "⚠️ Módulo de economía no disponible."
    def procesar_cofre(u, m, r, t): return m, r, t, "⚠️ Módulo de economía no disponible."
    def procesar_crimen(u, m, t): return m, t, "⚠️ Módulo de economía no disponible."
    def procesar_depositar(m, b, c): return m, b, "⚠️ Módulo de economía no disponible."
    def procesar_retirar(m, b, c): return m, b, "⚠️ Módulo de economía no disponible."
    def procesar_banco(m, b): return m, b, "⚠️ Módulo de economía no disponible."
    def procesar_Mercado(m, b, p): return "🛒 *MERCADO GENERAL*\n• `.mercado` - Ver artículos disponibles."
    def procesar_comprar_pokeballs(p): return "🛍️ *TIENDA POKÉMON*\n• `.comprar <item>` - Adquiere artículos."

def ejecutar_bot():
    global base_datos, datos_usuario, monedas_usuario, banco_usuario, racha_usuario, ultimo_trabajo, ultimo_diario, ultimo_cofre, ultimo_crimen, coleccion_museo

    # Menú Principal
    if mensaje_recibido in [".menu", ".help"]:
        return mostrar_menu()

    elif mensaje_recibido == ".adminmenu":
        return procesar_adminmenu()

    # Economía / Gacha (Con sus tiempos correctos)
    elif mensaje_recibido in [".crimen", ".crime"]:
        monedas_usuario, ultimo_crimen, respuesta = procesar_crimen(usuario_id, monedas_usuario, ultimo_crimen)
        datos_usuario["monedas"] = monedas_usuario
        datos_usuario["ultimo_crimen"] = ultimo_crimen
        guardar_todos_los_datos(base_datos)
        return respuesta

    elif mensaje_recibido in [".trabajar", ".work", ".w", ".wb"]:
        monedas_usuario, ultimo_trabajo, respuesta = procesar_trabajar(usuario_id, monedas_usuario, ultimo_trabajo)
        datos_usuario["monedas"] = monedas_usuario
        datos_usuario["ultimo_trabajo"] = ultimo_trabajo
        guardar_todos_los_datos(base_datos)
        return respuesta

    elif mensaje_recibido in [".cofre", ".daily"]:
        if mensaje_recibido == ".daily":
            monedas_usuario, racha_usuario, ultimo_diario, respuesta = procesar_diario(usuario_id, monedas_usuario, racha_usuario, ultimo_diario)
            datos_usuario["ultimo_diario"] = ultimo_diario
        else:
            monedas_usuario, racha_usuario, ultimo_cofre, respuesta = procesar_cofre(usuario_id, monedas_usuario, racha_usuario, ultimo_cofre)
            datos_usuario["ultimo_cofre"] = ultimo_cofre
        datos_usuario["monedas"] = monedas_usuario
        datos_usuario["racha"] = racha_usuario
        guardar_todos_los_datos(base_datos)
        return respuesta

    elif mensaje_recibido in [".depositar", ".dep", ".d"]:
        cantidad = parametro.lower()
        if cantidad == "all" or cantidad == "todo":
            cantidad_num = monedas_usuario
        else:
            try:
                cantidad_num = int(cantidad)
            except ValueError:
                cantidad_num = 0
        
        monedas_usuario, banco_usuario, respuesta = procesar_depositar(monedas_usuario, banco_usuario, cantidad_num)
        datos_usuario["monedas"] = monedas_usuario
        datos_usuario["banco"] = banco_usuario
        guardar_todos_los_datos(base_datos)
        return respuesta

    elif mensaje_recibido in [".retirar", ".ret", ".r"]:
        cantidad = parametro.lower()
        if cantidad == "all" or cantidad == "todo":
            cantidad_num = banco_usuario
        else:
            try:
                cantidad_num = int(cantidad)
            except ValueError:
                cantidad_num = 0
        
        monedas_usuario, banco_usuario, respuesta = procesar_retirar(monedas_usuario, banco_usuario, cantidad_num)
        datos_usuario["monedas"] = monedas_usuario
        datos_usuario["banco"] = banco_usuario
        guardar_todos_los_datos(base_datos)
        return respuesta

    elif mensaje_recibido in [".banco", ".bank"]:
        monedas_usuario, banco_usuario, respuesta = procesar_banco(monedas_usuario, banco_usuario)
        return respuesta

    elif mensaje_recibido == ".mercado":
        return procesar_Mercado(monedas_usuario, banco_usuario, parametro)
    elif mensaje_recibido == ".comprar":
        return procesar_comprar_pokeballs(parametro)

    # Comandos de Perfil y Usuario
    elif mensaje_recibido == ".perfil":
        return procesar_perfil(datos_usuario)
    elif mensaje_recibido == ".setname":
        return procesar_setname(parametro, datos_usuario, guardar_todos_los_datos, base_datos)
    elif mensaje_recibido == ".setdesc":
        return procesar_setdesc(parametro, datos_usuario, guardar_todos_los_datos, base_datos)
    elif mensaje_recibido == ".setage":
        return procesar_setage(parametro, datos_usuario, guardar_todos_los_datos, base_datos)
    elif mensaje_recibido == ".setbirth":
        return procesar_setbirth(parametro, datos_usuario, guardar_todos_los_datos, base_datos)
    elif mensaje_recibido == ".setgene":
        return procesar_setgene(parametro, datos_usuario, guardar_todos_los_datos, base_datos)
    elif mensaje_recibido == ".level":
        return procesar_level(datos_usuario)
    elif mensaje_recibido == ".levelup":
        return procesar_levelup(datos_usuario)

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
    elif mensaje_recibido in [".close", ".open", ".antilink", ".antispam", ".tagall", ".boton", ".botoff"]:
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

    # Pokémon
    elif mensaje_recibido == ".mispokemon":
        mis_pokemones = datos_usuario.get("pokemons", [])
        return procesar_Mispokemon(mis_pokemones)
    elif mensaje_recibido == ".mochila":
        return procesar_mochila([])
    elif mensaje_recibido == ".tienda":
        return procesar_tienda()
    elif mensaje_recibido == ".topokemon":
        return procesar_topokemon([])
    elif mensaje_recibido in [".capturar", ".cap"]:
        return procesar_capturar(parametro)
        
    else:
        return f"❓ Comando '{mensaje_recibido}' no reconocido. Usa *.menu* para ver la lista."

if __name__ == "__main__":
    try:
        resultado = ejecutar_bot()
        if resultado:
            print(resultado)
    except Exception as error:
        print(f"⚠️ Error al ejecutar el comando en Python: {str(error)}")
