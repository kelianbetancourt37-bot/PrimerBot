import random
import time

# Diccionarios para almacenar los tiempos de la última ejecución por usuario
cooldowns_trabajar = {}
cooldowns_diario = {}
cooldowns_cofre = {}
cooldowns_crimen = {}

def procesar_trabajar(usuario_id, monedas_actuales):
    tiempo_actual = time.time()
    tiempo_espera = 60  # Cooldown de 60 segundos (1 minuto)
    
    if usuario_id in cooldowns_trabajar:
        tiempo_transcurrido = tiempo_actual - cooldowns_trabajar[usuario_id]
        if tiempo_transcurrido < tiempo_espera:
            tiempo_restante = int(tiempo_espera - tiempo_transcurrido)
            return monedas_actuales, f"⏳ Estás cansado. Debes esperar *{tiempo_restante} segundos* para volver a trabajar."

    cooldowns_trabajar[usuario_id] = tiempo_actual
    ganancia = random.randint(10, 50)
    total = monedas_actuales + ganancia
    mensaje = f"👷‍♂️ ¡Trabajaste duro y ganaste {ganancia} monedas! Total: {total}"
    return total, mensaje


def procesar_diario(usuario_id, monedas_actuales, racha_actual):
    tiempo_actual = time.time()
    tiempo_espera = 86400  # Cooldown de 24 horas (86400 segundos)
    
    if usuario_id in cooldowns_diario:
        tiempo_transcurrido = tiempo_actual - cooldowns_diario[usuario_id]
        if tiempo_transcurrido < tiempo_espera:
            tiempo_restante = int(tiempo_espera - tiempo_transcurrido)
            horas = tiempo_restante // 3600
            minutos = (tiempo_restante % 3600) // 60
            return monedas_actuales, racha_actual, f"⏳ ¡Ya reclamaste tu recompensa diaria! Vuelve en *{horas} horas y {minutos} minutos*."

    cooldowns_diario[usuario_id] = tiempo_actual
    racha_actual += 1
    recompensa = 100 + (racha_actual * 20)
    total = monedas_actuales + recompensa
    mensaje = (
        f"🎁 ¡Recompensa diaria reclamada con éxito!\n"
        f"🔥 Llevas una racha de {racha_actual} día(s).\n"
        f"💵 Ganaste {recompensa} monedas. Total: {total}"
    )
    return total, racha_actual, mensaje


def procesar_cofre(usuario_id, monedas_actuales, racha_actual):
    tiempo_actual = time.time()
    tiempo_espera = 43200  # Cooldown de 12 horas (43200 segundos)
    
    if usuario_id in cooldowns_cofre:
        tiempo_transcurrido = tiempo_actual - cooldowns_cofre[usuario_id]
        if tiempo_transcurrido < tiempo_espera:
            tiempo_restante = int(tiempo_espera - tiempo_transcurrido)
            horas = tiempo_restante // 3600
            minutos = (tiempo_restante % 3600) // 60
            return monedas_actuales, racha_actual, f"⏳ ¡El cofre aún está cerrado con cerrojo! Espera *{horas} horas y {minutos} minutos*."

    cooldowns_cofre[usuario_id] = tiempo_actual
    racha_actual += 1
    recompensa = 200 + (racha_actual * 50)
    total = monedas_actuales + recompensa
    mensaje = (
        f"📦 ¡Abriste el cofre del tesoro!\n"
        f"🔥 Racha actual: {racha_actual} día(s).\n"
        f"💎 Ganaste {recompensa} monedas. Total: {total}"
    )
    return total, racha_actual, mensaje
    

def procesar_crimen(usuario_id, monedas_actuales):
    tiempo_actual = time.time()
    tiempo_espera = 300  # Cooldown de 5 minutos (300 segundos)
    
    if usuario_id in cooldowns_crimen:
        tiempo_transcurrido = tiempo_actual - cooldowns_crimen[usuario_id]
        if tiempo_transcurrido < tiempo_espera:
            tiempo_restante = int(tiempo_espera - tiempo_transcurrido)
            minutos = tiempo_restante // 60
            segundos = tiempo_restante % 60
            return monedas_actuales, f"⏳ La policía sigue patrullando la zona. Esconde tu rastro y espera *{minutos} min y {segundos} seg*."

    cooldowns_crimen[usuario_id] = tiempo_actual
    exito = random.choice([True, False])
    
    if exito:
        ganancia = random.randint(50, 150)
        total = monedas_actuales + ganancia
        mensaje = f"🥷 ¡Cometiste un crimen exitoso y ganaste {ganancia} monedas! Total: {total}"
        return total, mensaje
    else:
        multa = random.randint(30, 80)
        total = max(0, monedas_actuales - multa)
        mensaje = f"👮‍♂️ ¡Te atrapó la policía intentando cometer el crimen y perdiste {multa} monedas en multas! Total: {total}"
        return total, mensaje


def procesar_depositar(monedas_actuales, banco_actual, cantidad):
    if cantidad <= 0:
        return monedas_actuales, banco_actual, "❌ La cantidad a depositar debe ser mayor que cero."
    
    if cantidad > monedas_actuales:
        return monedas_actuales, banco_actual, f"❌ No tienes suficientes monedas en mano. Tienes: {monedas_actuales}."
    
    monedas_actuales -= cantidad
    banco_actual += cantidad
    
    mensaje = f"💰 Has depositado *{cantidad}* monedas en el banco.\n💵 En mano: {monedas_actuales} | 🏦 Banco: {banco_actual}"
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
