import random

# Lista de reliquias disponibles con su costo y rareza
RELIQUIAS = [
    {"nombre": "💎 Flor de la Luna", "precio": 10},
    {"nombre": "⚔️ Hacha de la Muerte", "precio": 50},
    {"nombre": "💉 Lágrima de la Muerte", "precio": 100},
    {"nombre": "🔪 Hacha de la Tortura", "precio": 200},
    {"nombre": "🗡️ Lágrima de la Tortura", "precio": 400},
    {"nombre": "🖼️ Monalisa de Hacendado", "precio": 150},
    {"nombre": "🗿 Estatua de Piedra Antigua", "precio": 300},
    {"nombre": "👑 Corona de Oro Perdida", "precio": 600},
    {"nombre": "🏺 Jarrón Histórico", "precio": 200}
]

def obtener_museo(coleccion_usuario):
    if not coleccion_usuario:
        return "🏛️ **Tu Museo está vacío.** ¡Usa `.comprarmuseo` para obtener tu primera pieza!"
    
    lista = "\n".join([f"- {pieza}" for pieza in coleccion_usuario])
    return f"🏛️ **Colección de tu Museo:**\n{lista}"

def comprar_reliquia(monedas_actuales, coleccion_usuario):
    reliquia = random.choice(RELIQUIAS)
    
    if monedas_actuales < reliquia["precio"]:
        return (
            monedas_actuales, 
            coleccion_usuario, 
            f"❌ Necesitas {reliquia['precio']} monedas para comprar '{reliquia['nombre']}'. Tienes: {monedas_actuales}."
        )
    
    monedas_actuales -= reliquia["precio"]
    coleccion_usuario.append(reliquia["nombre"])
    
    mensaje = (
        f"🏛️ **¡Nueva adquisición para el Museo!**\n"
        f"Compraste: {reliquia['nombre']} por {reliquia['precio']} monedas.\n"
        f"Monedas restantes: {monedas_actuales}"
    )
    return monedas_actuales, coleccion_usuario, mensaje
