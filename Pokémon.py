import random

# Listas de Pokémon disponibles para encontrar o regalar
LISTA_POKEMON_GENERAL = ["Pikachu", "Charmander", "Squirtle", "Bulbasaur", "Jigglypuff", "Snorlax", "Eevee", "Gengar", "Lucario", "Psyduck"]
LISTA_MOCHILAS = ["Mochila básica", "Mochila escolar", "Mochila de aventurero", "Mochila espacial"]
LISTA_TIENDA = ["¡Bienvenido a la PokéTienda!", "Has entrado a la tienda general."]

def procesar_Mispokemon(ver_pokemon):
    # Si la lista está vacía, evitamos que falle
    if not ver_pokemon:
        ver_pokemon = LISTA_POKEMON_GENERAL
    pokemon = random.choice(ver_pokemon)
    mensaje = f"🐱‍💻 Mis pokémon: {pokemon}"
    return mensaje

def procesar_mochila(ver_mochila):
    if not ver_mochila:
        ver_mochila = LISTA_MOCHILAS
    mochila = random.choice(ver_mochila)
    mensaje = f"👜 Mis mochilas: {mochila}"
    return mensaje

def procesar_topokemon(ver_pokemon, usuario_nombre="Entrenador"):
    if not ver_pokemon:
        ver_pokemon = LISTA_POKEMON_GENERAL
    pokemon = random.choice(ver_pokemon)
    mensaje = f"🐱‍💻 Top pokémon de {usuario_nombre}: {pokemon}"
    return mensaje

def procesar_tienda(pokeball=10, superpokeball=5, ultrapokeball=2, pocion_de_experiencia=3):
    mensaje = (
        f"🛒 *Tienda Pokémon*\n"
        f"🔴 Pokéballs: {pokeball}\n"
        f"🔵 Superpokeballs: {superpokeball}\n"
        f"🟡 Ultrapokeballs: {ultrapokeball}\n"
        f"🧪 Pociones de experiencia: {pocion_de_experiencia}"
        f"\n\n¡Bienvenido a la tienda de pokémones!"
        f"\n Usa `.comprar <Pokeballs>` para comprar Pokéballs."
    )
    return mensaje
