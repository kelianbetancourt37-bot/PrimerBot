import random

def procesar_comprarmuseo(monedas_actuales, coleccion_usuario):
    # Lista de posibles reliquias para comprar
    reliquias_disponibles = [
        "Jarrón Azteca", "Moneda de Oro", "Fragmento de Meteorito", 
        "Espada Antigua", "Libro Prohibido", "Estatua de la Vecindad"
    ]
    
    # 1. Verificar si tiene dinero
    costo = 50
    if monedas_actuales < costo:
        return monedas_actuales, coleccion_usuario, f"❌ No tienes suficientes monedas. Necesitas *{costo}* para una reliquia."
    
    # 2. Elegir una reliquia al azar
    nueva_reliquia = random.choice(reliquias_disponibles)
    
    # 3. Aplicar costo y actualizar colección
    monedas_actuales -= costo
    
    # Si la lista es None, la inicializamos
    if coleccion_usuario is None:
        coleccion_usuario = []
        
    coleccion_usuario.append(nueva_reliquia)
    
    mensaje = (
        f"🏛️ **¡COMPRA EXITOSA!** 🏛️\n\n"
        f"Has adquirido: *{nueva_reliquia}*\n"
        f"Costo: {costo} monedas.\n"
        f"Monedas restantes: *{monedas_actuales}*\n"
        f"Tu museo ahora tiene: {', '.join(coleccion_usuario)}"
    )
    
    return monedas_actuales, coleccion_usuario, mensaje