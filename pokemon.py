import random

LISTA_POKEMON_GENERAL = [
    "Pikachu", "Charmander", "Squirtle", "Bulbasaur", "Jigglypuff", 
    "Gengar", "Snorlax", "Eevee", "Lucario", "Mewtwo", 
    "Charizard", "Blastoise", "Venusaur", "Psyduck", "Machop", 
    "Abra", "Gastly", "Onix", "Cubone", "Rhydon", 
    "Chansey", "Kangaskhan", "Scyther", "Electabuzz", "Magmar", 
    "Magikarp", "Gyarados", "Lapras", "Ditto", "Vaporeon", 
    "Jolteon", "Flareon", "Porygon", "Aerodactyl", "Articuno", 
    "Zapdos", "Moltres", "Dratini", "Dragonite", "Mew", 
    "Chikorita", "Cyndaquil", "Totodile", "Togepi", "Ampharos", 
    "Marill", "Espeon", "Umbreon", "Tyranitar", "Celebi"
]
LISTA_MOCHILAS = ["Mochila básica", "Mochila escolar", "Mochila de aventurero", "Mochila espacial"]
LISTA_TIENDA = ["¡Bienvenido a la PokéTienda!", "Has entrado a la tienda general."]

IMAGENES_POKEMON = {
    "Pikachu": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
    "Charmander": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/4.png",
    "Squirtle": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/7.png",
    "Bulbasaur": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png",
    "Jigglypuff": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png",
    "Gengar": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png",
    "Snorlax": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/143.png",
    "Eevee": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
    "Lucario": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png",
    "Mewtwo": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
    "Charizard": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
    "Blastoise": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png",
    "Venusaur": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/3.png",
    "Psyduck": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/54.png",
    "Machop": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/66.png",
    "Abra": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/63.png",
    "Gastly": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/92.png",
    "Onix": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/95.png",
    "Cubone": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/104.png",
    "Rhydon": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/112.png",
    "Chansey": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/113.png",
    "Kangaskhan": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/115.png",
    "Scyther": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/123.png",
    "Electabuzz": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/125.png",
    "Magmar": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/126.png",
    "Magikarp": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/129.png",
    "Gyarados": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/130.png",
    "Lapras": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/131.png",
    "Ditto": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/132.png",
    "Vaporeon": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/134.png",
    "Jolteon": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/135.png",
    "Flareon": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/136.png",
    "Porygon": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/137.png",
    "Aerodactyl": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/142.png",
    "Articuno": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/144.png",
    "Zapdos": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/145.png",
    "Moltres": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/146.png",
    "Dratini": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/147.png",
    "Dragonite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/149.png",
    "Mew": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/151.png",
    "Chikorita": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/152.png",
    "Cyndaquil": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/155.png",
    "Totodile": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/158.png",
    "Togepi": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/175.png",
    "Ampharos": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/181.png",
    "Marill": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/183.png",
    "Espeon": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/196.png",
    "Umbreon": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/197.png",
    "Tyranitar": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/248.png",
    "Celebi": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/251.png"
}

PRECIOS_TIENDAPOKEMON = {
    "pokeball": 100,
    "superpokeball": 500,
    "ultrapokeball": 2000,
    "pocion_de_experiencia": 300
}

def procesar_Mispokemon(mis_pokemones):
    if not mis_pokemones:
        return "📦 No tienes ningún Pokémon atrapado aún. Usa `.capturar` para conseguir uno."
    
    lista = "\n".join([f"• {p}" for p in mis_pokemones])
    return f"🎒 *TUS POKÉMON CAPTURADOS*\n\n{lista}"

def procesar_mochila(usuario_nombre, pokeballs_restantes=0):
    return f"🎒 *MOCHILA*\n• Pokébolas: {pokeballs_restantes}"

def procesar_topokemon(ranking_usuarios):
    if not ranking_usuarios:
        return "🏆 *TOP POKÉMON*\n\nAún no hay entrenadores en el ranking."
    
    mensaje = "🏆 *TOP ENTRENADORES (Más Pokémon)*\n\n"
    for index, (nombre, cantidad) in enumerate(ranking_usuarios[:5], 1):
        mensaje += f"{index}. {nombre} — *{cantidad}* Pokémon\n"
        
    return mensaje

def procesar_capturar(capturar=None):
    if not capturar or capturar.capitalize() not in IMAGENES_POKEMON:
        capturar = random.choice(list(IMAGENES_POKEMON.keys()))
    else:
        capturar = capturar.capitalize()
    
    imagen_url = IMAGENES_POKEMON[capturar]
    mensaje = f"🐱‍💻 ¡Has capturado a un *{capturar}*!\n[IMAGEN:{imagen_url}]"
    
    return {
        "pokemon": capturar,
        "mensaje": mensaje
    }
    
def procesar_tiendapokemon(pokeball=10, superpokeball=5, ultrapokeball=2, pocion_de_experiencia=3):
    return (
        f"🛒 *Tienda Pokémon*\n"
        f"🔴 Pokéballs: {pokeball}\n"
        f"🔵 Superpokeballs: {superpokeball}\n"
        f"🟡 Ultrapokeballs: {ultrapokeball}\n"
        f"🧪 Pociones de experiencia: {pocion_de_experiencia}\n\n"
        f"¡Bienvenido a la tienda de pokémones!\n"
        f"Usa `.comprar <cantidad>` para adquirir artículos."
    )