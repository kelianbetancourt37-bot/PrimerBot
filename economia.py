import random
import time

PRECIOS_MERCADO = {
    "botellas_de_experiencia": 500,
    "espada_de_la_lucha": 1000,
    "espada_de_la_vitalidad": 2000,
    "espada_de_la_salud": 3000,
    "hacha_divina_escanor": 5000
}

def procesar_trabajar(usuario_id, monedas_actuales, ultimo_trabajo):
    tiempo_actual = time.time()
    tiempo_espera = 300  # 5 minutos exactos de cooldown
    
    if ultimo_trabajo > 0:
        tiempo_transcurrido = tiempo_actual - ultimo_trabajo
        if tiempo_transcurrido < tiempo_espera:
            tiempo_restante = int(tiempo_espera - tiempo_transcurrido)
            minutos = tiempo_restante // 60
            segundos = tiempo_restante % 60
            return monedas_actuales, ultimo_trabajo, f"⏳ Estás cansado. Debes esperar *{minutos} min y {segundos} seg* para volver a trabajar."

    ganancia = random.randint(10, 50)
    total = monedas_actuales + ganancia
    mensaje = f"👷‍♂️ ¡Trabajaste duro y ganaste {ganancia} monedas! Total: {total}"
    return total, tiempo_actual, mensaje


def procesar_diario(usuario_id, monedas_actuales, racha_actual, ultimo_diario):
    tiempo_actual = time.time()
    tiempo_espera = 86400  # 24 horas exactas
    
    if ultimo_diario > 0:
        tiempo_transcurrido = tiempo_actual - ultimo_diario
        if tiempo_transcurrido < tiempo_espera:
            tiempo_restante = int(tiempo_espera - tiempo_transcurrido)
            horas = tiempo_restante // 3600
            minutos = (tiempo_restante % 3600) // 60
            return monedas_actuales, racha_actual, ultimo_diario, f"⏳ ¡Ya reclamaste tu recompensa diaria! Vuelve en *{horas} horas y {minutos} minutos*."

    racha_actual += 1
    recompensa = 100 + (racha_actual * 20)
    total = monedas_actuales + recompensa
    mensaje = (
        f"🎁 ¡Recompensa diaria reclamada con éxito!\n"
        f"🔥 Llevas una racha de {racha_actual} día(s).\n"
        f"💵 Ganaste {recompensa} monedas. Total: {total}"
    )
    return total, racha_actual, tiempo_actual, mensaje


def procesar_cofre(usuario_id, monedas_actuales, racha_actual, ultimo_cofre):
    tiempo_actual = time.time()
    tiempo_espera = 86400  # 24 horas exactas
    
    if ultimo_cofre > 0:
        tiempo_transcurrido = tiempo_actual - ultimo_cofre
        if tiempo_transcurrido < tiempo_espera:
            tiempo_restante = int(tiempo_espera - tiempo_transcurrido)
            horas = tiempo_restante // 3600
            minutos = (tiempo_restante % 3600) // 60
            return monedas_actuales, racha_actual, ultimo_cofre, f"⏳ ¡El cofre aún está cerrado! Espera *{horas} horas y {minutos} minutos*."

    racha_actual += 1
    recompensa = 200 + (racha_actual * 50)
    total = monedas_actuales + recompensa
    mensaje = (
        f"📦 ¡Abriste el cofre del tesoro!\n"
        f"🔥 Racha actual: {racha_actual} día(s).\n"
        f"💎 Ganaste {recompensa} monedas. Total: {total}"
    )
    return total, racha_actual, tiempo_actual, mensaje
    

def procesar_crimen(usuario_id, monedas_actuales, ultimo_crimen):
    tiempo_actual = time.time()
    tiempo_espera = 300  # 5 minutos
    
    if ultimo_crimen > 0:
        tiempo_transcurrido = tiempo_actual - ultimo_crimen
        if tiempo_transcurrido < tiempo_espera:
            tiempo_restante = int(tiempo_espera - tiempo_transcurrido)
            minutos = tiempo_restante // 60
            segundos = tiempo_restante % 60
            return monedas_actuales, ultimo_crimen, f"⏳ La policía sigue patrullando. Espera *{minutos} min y {segundos} seg*."

    exito = random.choice([True, False])
    if exito:
        ganancia = random.randint(50, 150)
        total = monedas_actuales + ganancia
        mensaje = f"🥷 ¡Crimen exitoso! Ganaste {ganancia} monedas. Total: {total}"
        return total, tiempo_actual, mensaje
    else:
        multa = random.randint(30, 80)
        total = max(0, monedas_actuales - multa)
        mensaje = f"👮‍♂️ ¡Te atrapó la policía! Perdiste {multa} monedas. Total: {total}"
        return total, tiempo_actual, mensaje


def procesar_depositar(monedas_actuales, banco_actual, cantidad):
    if cantidad <= 0:
        return monedas_actuales, banco_actual, "❌ La cantidad a depositar debe ser mayor que cero."
    if cantidad > monedas_actuales:
        return monedas_actuales, banco_actual, f"❌ No tienes suficientes monedas en mano. Tienes: {monedas_actuales}."
    
    monedas_actuales -= cantidad
    banco_actual += cantidad
    mensaje = f"💰 Has depositado *{cantidad}* monedas en el banco.\n💵 En mano: {monedas_actuales} | 🏦 Banco: {banco_actual}"
    return monedas_actuales, banco_actual, mensaje


def procesar_retirar(monedas_actuales, banco_actual, cantidad):
    if cantidad <= 0:
        return monedas_actuales, banco_actual, "❌ La cantidad a retirar debe ser mayor que cero."
    if cantidad > banco_actual:
        return monedas_actuales, banco_actual, f"❌ No tienes suficiente dinero en el banco. Tienes: {banco_actual}."
    
    banco_actual -= cantidad
    monedas_actuales += cantidad
    mensaje = f"💰 Has retirado *{cantidad}* monedas del banco.\n💵 En mano: {monedas_actuales} | 🏦 Banco: {banco_actual}"
    return monedas_actuales, banco_actual, mensaje


def procesar_banco(monedas_mano, monedas_banco):
    if monedas_banco > 0:
        mensaje = (
            f"🏦 *ESTADO DE TU CUENTA BANCARIA*\n\n"
            f"💵 Dinero en mano: *{monedas_mano}* monedas\n"
            f"💰 Dinero en el banco: *{monedas_banco}* monedas\n"
            f"💎 Total general: *{monedas_mano + monedas_banco}* monedas"
        )
    else:
        mensaje = (
            f"🏦 *ESTADO DE TU CUENTA BANCARIA*\n\n"
            f"💵 Dinero en mano: *{monedas_mano}* monedas\n"
            f"💰 Dinero en el banco: *0* monedas\n"
            f"⚠️ *Tu cuenta bancaria está vacía.* Usa `.depositar [cantidad]` para guardar dinero."
        )
    return monedas_mano, monedas_banco, mensaje


def procesar_Mercado(monedas_actuales, banco_actual, parametro=""):
    return (
        "🛒 *MERCADO DE JASPER* 🛒\n\n"
        "┃  • *Botellas de experiencia:* 500 monedas (`.comprar botellas_de_experiencia`)\n"
        "┃  • *Espada de la lucha:* 1,000 monedas (`.comprar espada_de_la_lucha`)\n"
        "┃  • *Espada de la vitalidad:* 2,000 monedas (`.comprar espada_de_la_vitalidad`)\n"
        "┃  • *Espada de la salud:* 3,000 monedas (`.comprar espada_de_la_salud`)\n"
        "┃  • *Hacha divina Escanor:* 5,000 monedas (`.comprar hacha_divina_escanor`)\n\n"
        "_Usa `.comprar <objeto>` para adquirir algo._"
    )

def procesar_comprar_pokeballs(parametro=""):
    if not parametro:
        return "⚠️ Especifica qué objeto deseas comprar del mercado. Ejemplo: `.comprar espada_de_la_lucha`"
    
    parametro_limpio = parametro.lower().strip()
    if parametro_limpio in PRECIOS_MERCADO:
        precio = PRECIOS_MERCADO[parametro_limpio]
        return f"✅ Has adquirido *{parametro}* por un costo de *{precio}* monedas."
    else:
        return f"❌ El objeto '{parametro}' no existe en el mercado. Revisa los nombres con `.mercado`."

def procesar_inventario(usuario_id, datos_usuario):
    monedas = datos_usuario.get("monedas", 500)
    banco = datos_usuario.get("banco", 0)
    racha = datos_usuario.get("racha", 0)
    inventario_items = datos_usuario.get("inventario", [])
    
    items_texto = ", ".join(inventario_items) if inventario_items else "Vacío"
    
    return (
        f"🎒 *INVENTARIO DE USUARIO*\n\n"
        f"👤 ID: `{usuario_id}`\n"
        f"💵 Monedas en mano: *{monedas}*\n"
        f"🏦 Monedas en banco: *{banco}*\n"
        f"🔥 Racha: *{racha}*\n"
        f"📦 Objetos: *{items_texto}*"
    )
