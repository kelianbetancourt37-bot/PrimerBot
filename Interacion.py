import random

def saludar(usuario=""):
    gifs = [
        "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.mp4",
        "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.mp4",
        "https://media.giphy.com/media/xT9IgG50Fb7Mi0prBC/giphy.mp4"
    ]
    gif = random.choice(gifs)
    texto = f"👋 ¡Hola {usuario}!" if usuario else "👋 ¡Hola a todos!"
    return f"GIF|{gif}|{texto}"

def beso(usuario=""):
    gifs = [
        "https://media.giphy.com/media/3o7TKsZr9aJ6f0k5QY/giphy.mp4",
        "https://media.giphy.com/media/13HgwGsXF0ai24/giphy.mp4"
    ]
    gif = random.choice(gifs)
    texto = f"😘 ¡Un beso para {usuario}!" if usuario else "😘 ¡Un beso al aire!"
    return f"GIF|{gif}|{texto}"

def abrazo(usuario=""):
    gifs = [
        "https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.mp4"
    ]
    gif = random.choice(gifs)
    texto = f"🤗 ¡Un fuerte abrazo para {usuario}!" if usuario else "🤗 ¡Un abrazo para todos!"
    return f"GIF|{gif}|{texto}"

def golpe(usuario=""):
    gifs = [
        "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.mp4"
    ]
    gif = random.choice(gifs)
    texto = f"👊 ¡Un golpe para {usuario}!" if usuario else "👊 ¡Un golpe al aire!"
    return f"GIF|{gif}|{texto}"

def caricia(usuario=""):
    gifs = [
        "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.mp4"
    ]
    gif = random.choice(gifs)
    texto = f"🥰 Una caricia para {usuario}" if usuario else "🥰 Una caricia"
    return f"GIF|{gif}|{texto}"

def eliminar(usuario=""):
    gifs = [
        "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.mp4"
    ]
    gif = random.choice(gifs)
    texto = f"💀 ¡{usuario} ha sido eliminado!" if usuario else "💀 ¡Eliminado!"
    return f"GIF|{gif}|{texto}"

def correr(usuario=""):
    gifs = [
        "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.mp4"
    ]
    gif = random.choice(gifs)
    texto = f"🏃‍♂️ ¡Corriendo de {usuario}!" if usuario else "🏃‍♂️ ¡Corriendo!"
    return f"GIF|{gif}|{texto}"
