import random

def procesar_saludar(usuario):
    salodar = random.choice([
        mostrar_gif_saludo(),
        f"¡Hola {usuario}! 👋",
    ])
    return salodar

def mostrar_gif_saludo():
    gifs_saludo = [
        "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif",
        "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
        "https://media.giphy.com/media/xT9IgG50Fb7Mi0prBC/giphy.gif",
        "https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif",
        "https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif",
    ]
    return random.choice(gifs_saludo)

def procesar_beso(usuario):
    beso = random.choice([
        mostrar_gif_beso(),
        f"¡{usuario}, te envío un beso! 😘",
    ])
    return beso

def mostrar_gif_beso():
    gifs_beso = [
        "https://media.giphy.com/media/3o7TKsZr9aJ6f0k5QY/giphy.gif",
        "https://media.giphy.com/media/13HgwGsXF0ai24/giphy.gif",
        "https://media.giphy.com/media/3o7TKsZr9aJ6f0k5QY/giphy.gif",
    ]
    return random.choice(gifs_beso)

def procesar_abrazo(usuario):
    abrazo = random.choice([
        mostrar_gif_abrazo(),
        f"¡{usuario}, te envío un abrazo! 🤗",
    ])
    return abrazo

def mostrar_gif_abrazo():
    gifs_abrazo = [
        "https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif",
        "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif",
        "https://media.giphy.com/media/xT9IgG50Fb7Mi0prBC/giphy.gif",
    ]
    return random.choice(gifs_abrazo)

def procesar_golpe(usuario):
    golpe = random.choice([
        mostrar_gif_golpe(),
        f"¡{usuario}, te he dado un golpe! 👊",
    ])
    return golpe

def mostrar_gif_golpe():
    gifs_golpe = [
        "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif",
        "https://media.giphy.com/media/xT9IgG50Fb7Mi0prBC/giphy.gif",
        "https://media.giphy.com/media/3o7TKsZr9aJ6f0k5QY/giphy.gif",
    ]
    return random.choice(gifs_golpe)

def procesar_caricia(usuario):
    caricia = random.choice([
        mostrar_gif_caricia(),
        f"¡{usuario}, te envío una caricia! 🥰",
    ])
    return caricia

def mostrar_gif_caricia():
    gifs_caricia = [
        "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif",
        "https://media.giphy.com/media/xT9IgG50Fb7Mi0prBC/giphy.gif",
        "https://media.giphy.com/media/3o7TKsZr9aJ6f0k5QY/giphy.gif",
    ]
    return random.choice(gifs_caricia)

def procesar_kill(usuario):
    kill = random.choice([
        mostrar_gif_kill(),
        f"¡{usuario}, has sido eliminado! 💀",
    ])
    return kill

def mostrar_gif_kill():
    gifs_kill = [
        "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif",
        "https://media.giphy.com/media/xT9IgG50Fb7Mi0prBC/giphy.gif",
        "https://media.giphy.com/media/3o7TKsZr9aJ6f0k5QY/giphy.gif",
    ]
    return random.choice(gifs_kill)

def procesar_correr(usuario):
    correr = random.choice([
        mostrar_gif_correr(),
        f"¡{usuario}, estás corriendo! 🏃‍♂️",
    ])
    return correr

def mostrar_gif_correr():
    gifs_correr = [
        "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif",
        "https://media.giphy.com/media/xT9IgG50Fb7Mi0prBC/giphy.gif",
        "https://media.giphy.com/media/3o7TKsZr9aJ6f0k5QY/giphy.gif",
    ]
    return random.choice(gifs_correr)