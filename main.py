class Videojuego:
    def __init__(self, titulo, genero, año, duracion, clasificacion, desarrollador):
        self.titulo = titulo
        self.genero = genero
        self.año = año
        self.duracion = duracion
        self.clasificacion = clasificacion
        self.desarrollador = desarrollador

    def __str__(self):
        return f"Título: {self.titulo}\nGénero: {', '.join(self.genero)}\nAño: {self.año}\nDuración: {self.duracion} horas\nClasificación: {', '.join(self.clasificacion)}\nDesarrollador: {', '.join(self.desarrollador)}"


class NodoArbol:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, valor):
        self.raiz = self._insertar_recursivo(self.raiz, clave, valor)

    def _insertar_recursivo(self, nodo_actual, clave, valor):
        if nodo_actual is None:
            return NodoArbol(clave, valor)
        if clave < nodo_actual.clave:
            nodo_actual.izquierda = self._insertar_recursivo(nodo_actual.izquierda, clave, valor)
        elif clave > nodo_actual.clave:
            nodo_actual.derecha = self._insertar_recursivo(nodo_actual.derecha, clave, valor)
        else:
            # Si la clave ya existe, actualizar el valor
            nodo_actual.valor = valor
        return nodo_actual

    def inorden(self):
        self._inorden_recursivo(self.raiz)

    def _inorden_recursivo(self, nodo_actual):
        if nodo_actual:
            self._inorden_recursivo(nodo_actual.izquierda)
            print(nodo_actual.valor)
            self._inorden_recursivo(nodo_actual.derecha)

    def por_nivel(self):
        if self.raiz is None:
            return
        cola = [self.raiz]
        while cola:
            nodo_actual = cola.pop(0)
            print(nodo_actual.valor)
            if nodo_actual.izquierda:
                cola.append(nodo_actual.izquierda)
            if nodo_actual.derecha:
                cola.append(nodo_actual.derecha)

    def buscar(self, clave):
        return self._buscar_recursivo(self.raiz, clave)

    def _buscar_recursivo(self, nodo_actual, clave):
        if nodo_actual is None or nodo_actual.clave == clave:
            return nodo_actual
        if clave < nodo_actual.clave:
            return self._buscar_recursivo(nodo_actual.izquierda, clave)
        return self._buscar_recursivo(nodo_actual.derecha, clave)


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