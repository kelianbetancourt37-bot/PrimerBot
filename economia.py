import random

def procesar_trabajar(monedas_actuales):
    ganancia = random.randint(10, 50)
    total = monedas_actuales + ganancia
    mensaje = f"¡Trabajaste duro y ganaste {ganancia} monedas! Total: {total}"
    return total, mensaje

def procesar_diario(monedas_actuales, racha_actual):
    racha_actual += 1
    recompensa = 100 + (racha_actual * 20)
    total = monedas_actuales + recompensa
    
    mensaje = (
        f"¡Recompensa diaria reclamada! 🎁\n"
        f"Llevas una racha de {racha_actual} día(s).\n"
        f"Ganaste {recompensa} monedas. Total: {total}"
    )
    return total, racha_actual, mensaje

def procesar_cofre(monedas_actuales, racha_actual):
    racha_actual += 1
    recompensa = 200 + (racha_actual * 50)
    total = monedas_actuales + recompensa
    
    mensaje = (
        f"¡Cofre abierto! 🎁\n"
        f"Llevas una racha de {racha_actual} día(s).\n"
        f"Ganaste {recompensa} monedas. Total: {total}"
    )
    return total, racha_actual, mensaje

def procesar_crimen(monedas_actuales):
    exito = random.choice([True, False])
    if exito:
        ganancia = random.randint(50, 150)
        total = monedas_actuales + ganancia
        mensaje = f"¡Cometiste un crimen exitoso y ganaste {ganancia} monedas! Total: {total}"
    else:
        perdida = random.randint(20, 70)
        total = max(0, monedas_actuales - perdida)
        mensaje = f"¡El crimen falló! Perdiste {perdida} monedas. Total: {total}"
    
    return total, mensaje

def procesar_depositar(monedas_actuales, banco_actual, cantidad):
    if cantidad <= 0:
        return monedas_actuales, banco_actual, "❌ La cantidad a depositar debe ser mayor que cero."
    
    if cantidad > monedas_actuales:
        return monedas_actuales, banco_actual, f"❌ No tienes suficientes monedas para depositar. Tienes: {monedas_actuales}."
    
    monedas_actuales -= cantidad
    banco_actual += cantidad
    
    mensaje = f"💰 Has depositado {cantidad} monedas en el banco. Monedas actuales: {monedas_actuales}, Banco: {banco_actual}"
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
