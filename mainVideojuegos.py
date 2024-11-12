from Videojuego import Videojuego
from Arbol import Arbol


# Crear la lista de videojuegos
videojuegos = [
    Videojuego("The Legend of Zelda: Breath of the Wild", ["Aventura", "Acción"], 2017, 50, ["E"], ["Nintendo"]),
    Videojuego("The Witcher 3: Wild Hunt", ["RPG", "Aventura"], 2015, 100, ["M"], ["CD Projekt Red"]),
    Videojuego("Dark Souls", ["Acción", "RPG"], 2011, 60, ["M"], ["FromSoftware"]),
    Videojuego("Super Mario Odyssey", ["Plataformas", "Aventura"], 2017, 12, ["E"], ["Nintendo"]),
    Videojuego("God of War", ["Acción", "Aventura"], 2018, 25, ["M"], ["Santa Monica Studio"]),
    Videojuego("Minecraft", ["Supervivencia", "Construcción"], 2011, 100, ["E"], ["Mojang"]),
    Videojuego("Red Dead Redemption 2", ["Acción", "Aventura"], 2018, 60, ["M"], ["Rockstar Games"]),
    Videojuego("Overwatch", ["Disparos", "Multijugador"], 2016, 20, ["T"], ["Blizzard Entertainment"]),
    Videojuego("Final Fantasy VII Remake", ["RPG", "Acción"], 2020, 40, ["T"], ["Square Enix"]),
    Videojuego("Hollow Knight", ["Acción", "Aventura"], 2017, 30, ["E"], ["Team Cherry"])
]

# Crear el árbol por título y año
arbol_titulo_año = Arbol()
for juego in videojuegos:
    clave = (juego.titulo, juego.año)
    arbol_titulo_año.insertar(clave, juego)

# Crear el árbol por clasificación, título y año
arbol_clasificacion_titulo_año = Arbol()
for juego in videojuegos:
    for clasificacion in juego.clasificacion:
        clave = (clasificacion, juego.titulo, juego.año)
        arbol_clasificacion_titulo_año.insertar(clave, juego)

# Recorrido inorden del árbol por título y año
print("Recorrido inorden del árbol por título y año:")
arbol_titulo_año.inorden()

# Recorrido por nivel del árbol por clasificación
print("\nRecorrido por nivel del árbol por clasificación:")
arbol_clasificacion_titulo_año.por_nivel()

# Mostrar información de juegos específicos
print("\nInformación de juegos específicos:")
print(arbol_titulo_año.buscar(("The Legend of Zelda: Breath of the Wild", 2017)).valor)
print(arbol_titulo_año.buscar(("The Witcher 3: Wild Hunt", 2015)).valor)

# Mostrar juegos con clasificación "M"
print("\nJuegos con clasificación 'M':")
for juego in videojuegos:
    if "M" in juego.clasificacion:
        print(juego)

# Listar juegos con duración mayor a 50 horas
print("\nJuegos con duración mayor a 50 horas:")
for juego in videojuegos:
    if juego.duracion > 50:
        print(juego)

# Mostrar juegos del género "Acción" o "Aventura"
print("\nJuegos del género 'Acción' o 'Aventura':")
for juego in videojuegos:
    if "Acción" in juego.genero or "Aventura" in juego.genero:
        print(juego)

# Listar juegos que comienzan con "S" o contienen ":"
print("\nJuegos que comienzan con 'S' o contienen ':':")
for juego in videojuegos:
    if juego.titulo.startswith("S") or ":" in juego.titulo:
        print(juego)

# Crear índice por género
indice_genero = {}
for juego in videojuegos:
    for genero in juego.genero:
        if genero not in indice_genero:
            indice_genero[genero] = []
        indice_genero[genero].append(juego)

# Mostrar índice por género
print("\nÍndice por género:")
for genero, juegos in indice_genero.items():
    print(f"\nGénero: {genero}")
    for juego in juegos:
        print(juego.titulo)