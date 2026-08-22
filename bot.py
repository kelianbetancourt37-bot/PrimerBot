import sys
import os
import json

sys.stdout.reconfigure(encoding='utf-8')

# --- CONFIGURACIÓN DE BASE DE DATOS MULTIUSUARIO ---
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

# Argumentos de Node.js (aquí Node.js debe enviar el ID del usuario como argumento o lo simulamos)
args = sys.argv[1:]
mensaje_recibido = args[0].lower().strip() if len(args) > 0 else ".menu"
parametro = args[1].strip() if (len(args) > 1 and args[1] != "None") else ""

# NOTA: Idealmente Node.js debería pasar el ID del remitente como argumento. 
# Si por ahora no lo pasa, puedes usar un identificador temporal o extraerlo.
# Digamos que recibimos el ID del usuario en un argumento extra o usamos uno por defecto:
usuario_id = args[2].strip() if (len(args) > 2 and args[2] != "None") else "usuario_general"

# Si el usuario no existe en la base de datos, lo registramos automáticamente con valores iniciales
if usuario_id not in base_datos:
    base_datos[usuario_id] = {
        "monedas": 500,
        "banco": 0,
        "racha": 0
    }
    guardar_todos_los_datos(base_datos)

# Obtenemos los datos específicos de este usuario
datos_usuario = base_datos[usuario_id]
monedas_usuario = datos_usuario.get("monedas", 500)
banco_usuario = datos_usuario.get("banco", 0)
racha_usuario = datos_usuario.get("racha", 0)

# --- IMPORTACIONES SEGURAS ---
try:
    from menu import mostrar_menu
except ImportError:
    def mostrar_menu(): return "📜 *MENÚ PRINCIPAL*\nUsa .help para ayuda."

try:
    from economia import procesar_trabajar, procesar_diario, procesar_cofre, procesar_depositar, procesar_crimen, procesar_banco, procesar_retirar
except ImportError:
    pass

try:
    from descargas import procesar_pinterest, procesar_imagenes
except ImportError:
    pass

def ejecutar_bot():
    global base_datos, datos_usuario, monedas_usuario, banco_usuario, racha_usuario

    # Economía / Gacha
    if mensaje_recibido in [".crimen", ".crime"]:
        monedas_usuario, respuesta = procesar_crimen(usuario_id, monedas_usuario)
        datos_usuario["monedas"] = monedas_usuario
        guardar_todos_los_datos(base_datos)
        return respuesta

    elif mensaje_recibido in [".trabajar", ".work", ".w", ".wb"]:
        monedas_usuario, respuesta = procesar_trabajar(usuario_id, monedas_usuario)
        datos_usuario["monedas"] = monedas_usuario
        guardar_todos_los_datos(base_datos)
        return respuesta

    elif mensaje_recibido in [".cofre", ".daily"]:
        if mensaje_recibido == ".daily":
            monedas_usuario, racha_usuario, respuesta = procesar_diario(usuario_id, monedas_usuario, racha_usuario)
        else:
            monedas_usuario, racha_usuario, respuesta = procesar_cofre(usuario_id, monedas_usuario, racha_usuario)
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

    elif mensaje_recibido in [".banco", ".bank"]:
        monedas_usuario, banco_usuario, respuesta = procesar_banco(monedas_usuario, banco_usuario)
        return respuesta

    else:
        return f"❓ Comando '{mensaje_recibido}' no reconocido. Usa *.menu* para ver la lista."

if __name__ == "__main__":
    try:
        resultado = ejecutar_bot()
        if resultado:
            print(resultado)
    except Exception as error:
        print(f"⚠️ Error al ejecutar el comando en Python: {str(error)}")
