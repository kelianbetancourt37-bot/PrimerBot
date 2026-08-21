import sys
# 1. Importaciones del menú
from menu import mostrar_menu

# 2. Importaciones de economía, museo y administración
from comandos.economia import procesar_trabajar, procesar_diario, procesar_cofre
from comandos.museo import obtener_museo, comprar_reliquia
from comandos.admin import procesar_admin_command

# 3. Importaciones de interacción (asegúrate de ajustar la ruta si están en un subdirectorio)
from comandos.interaccion import saludar, beso, abrazo, golpe, eliminar, caricia, correr

# 4. Importaciones de gestión de grupos y descargas
from comandos.gestion import activar_desactivar_bienvenida, mostrar_reglas
from comandos.descargar import (
    descargar_mediafire, descargar_mega, descargar, descargar_facebook,
    descargar_instagram, descargar_tiktok, descargar_youtube,
    procesar_mp3, procesar_mp4, procesar_imagenes, procesar_sticker
)

# Variables del usuario
monedas_usuario = 500
racha_usuario = 0
coleccion_museo = []

# Lee los argumentos enviados desde la consola
args = sys.argv[1:]
mensaje_recibido = args[0] if len(args) > 0 else ".menu"
parametro = args[1] if len(args) > 1 else None

# Lógica de comandos
# Corregido: sintaxis correcta para evaluar múltiples opciones
if mensaje_recibido in [".menu", ".help"]:
    print(mostrar_menu())

elif mensaje_recibido in [".trabajar", ".work", ".w", ".wb"]:
    monedas_usuario, respuesta = procesar_trabajar(monedas_usuario)
    print(respuesta)

elif mensaje_recibido in [".daily", ".diario"]:
    monedas_usuario, racha_usuario, respuesta = procesar_diario(monedas_usuario, racha_usuario)
    print(respuesta)

elif mensaje_recibido == ".cofre":
    monedas_usuario, racha_usuario, respuesta = procesar_cofre(monedas_usuario, racha_usuario)
    print(respuesta)

elif mensaje_recibido == ".museo":
    print(obtener_museo(coleccion_museo))

elif mensaje_recibido == ".comprarmuseo":
    monedas_usuario, coleccion_museo, respuesta = comprar_reliquia(monedas_usuario, coleccion_museo)
    print(respuesta)

# Comandos de Administración
elif mensaje_recibido in [".ban", ".kick", ".silenciar", ".desilenciar"]:
    comando_limpio = mensaje_recibido.replace(".", "")
    print(procesar_admin_command(comando_limpio, user=parametro))

elif mensaje_recibido in [".close", ".open", ".antilink", ".antispam", ".tagall"]:
    comando_limpio = mensaje_recibido.replace(".", "")
    print(procesar_admin_command(comando_limpio))

elif mensaje_recibido == ".delete":
    print(procesar_admin_command("delete", mensaje_id=parametro))

# Comandos de interacción
elif mensaje_recibido == ".saludar":
    print(saludar(parametro))

elif mensaje_recibido == ".beso":
    print(beso(parametro))

elif mensaje_recibido == ".abrazo":
    print(abrazo(parametro))

elif mensaje_recibido == ".golpe":
    print(golpe(parametro))

elif mensaje_recibido == ".kill":
    print(eliminar(parametro))    

elif mensaje_recibido == ".caricia":
    print(caricia(parametro))

elif mensaje_recibido == ".correr":
    print(correr(parametro))

# Comandos de gestión de grupos
elif mensaje_recibido == ".welcome":
    print(activar_desactivar_bienvenida(parametro))

elif mensaje_recibido == ".reglas":
    print(mostrar_reglas())

# Comandos de descargas de medios
elif mensaje_recibido == ".mediafire":
    print(descargar_mediafire(parametro))

elif mensaje_recibido == ".mega":
    print(descargar_mega(parametro))

elif mensaje_recibido == ".descargar":
    print(descargar(parametro))

elif mensaje_recibido == ".facebook":
    print(descargar_facebook(parametro))

elif mensaje_recibido == ".instagram":
    print(descargar_instagram(parametro))

elif mensaje_recibido == ".tiktok":
    print(descargar_tiktok(parametro))

elif mensaje_recibido == ".youtube":
    print(descargar_youtube(parametro))

elif mensaje_recibido == ".mp3":
    print(procesar_mp3(parametro))

elif mensaje_recibido == ".mp4":
    print(procesar_mp4(parametro))

elif mensaje_recibido == ".imagen":
    print(procesar_imagenes(parametro))

elif mensaje_recibido == ".sticker":
    print(procesar_sticker(parametro))

else:
    print("Comando no reconocido. Usa .menu para ver la lista de comandos.")