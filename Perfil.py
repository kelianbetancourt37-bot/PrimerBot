import random.choice

def procesar_perfil(usuario=""):
    destino = usuario if usuario else "Vecino"
    
    # Lista de frases o apodos divertidos estilo la vecindad
    apodos = ["El Chavo del Ocho", "La Chilindrina", "Don Ramón", "Kiko", "Doña Florinda", "El Profesor Jirafales", "El Señor Barriga", "La Bruja del 71"]    
    apodo_aleatorio = random.choice(apodos)
    
    mensaje = (
        f"🏘️ *LA VECINDAD DEL BOT* 🏠\n\n"
        f"👤 *Inquilino:* *{destino}*\n"
        f"🏷️ *Apodo en la vecindad:* _{apodo_aleatorio}_\n"
        f"🏠 *Vivienda:* Casa número {random.randint(1, 74)}\n"
        f"📝 *Frase célebre:* \"¡Eso, eso, eso!\" o \"¡No te doy otra patada porque...\"\n"
        f"🎂 *Edad:* {random.randint(8, 60)} años (¡crujiendo los huesos!)\n"
        f"💰 *Deuda de la renta:* ${random.randint(0, 14)} meses con el Señor Barriga 💸\n"
        f"📊 *Nivel en la vecindad:* *Nivel 5* (Vecino honorable)"
    )
    return mensaje