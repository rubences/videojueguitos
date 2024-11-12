class Libro:
    def __init__(self, titulo, autor, año, paginas, genero, editorial):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.paginas = paginas
        self.genero = genero
        self.editorial = editorial

    def __str__(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nAño: {self.año}\nPáginas: {self.paginas}\nGénero: {self.genero}\nEditorial: {self.editorial}"


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


# Crear la lista de libros
libros = [
    Libro("Cien años de soledad", "Gabriel García Márquez", 1967, 496, "Novela", "Sudamericana"),
    Libro("1984", "George Orwell", 1949, 328, "Ciencia Ficción", "Secker & Warburg"),
    Libro("El Hobbit", "J.R.R. Tolkien", 1937, 310, "Fantasía", "George Allen & Unwin"),
    Libro("Crimen y castigo", "Fiódor Dostoievski", 1866, 672, "Novela", "The Russian Messenger"),
    Libro("El principito", "Antoine de Saint-Exupéry", 1943, 96, "Fantasía", "Reynal & Hitchcock"),
    Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, 863, "Novela", "Francisco de Robles"),
    Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", 1997, 223, "Fantasía", "Bloomsbury"),
    Libro("El retrato de Dorian Gray", "Oscar Wilde", 1890, 272, "Novela", "Ward, Lock & Company"),
    Libro("La Odisea", "Homero", -800, 344, "Poesía", "Desconocida"), 
    Libro("El nombre de la rosa", "Umberto Eco", 1980, 536, "Novela", "Bompiani") 
]

# Crear el árbol por título y año
arbol_titulo_año = Arbol()
for libro in libros:
    clave = (libro.titulo, libro.año)
    arbol_titulo_año.insertar(clave, libro)

# Crear el árbol por género, título y año
arbol_genero_titulo_año = Arbol()
for libro in libros:
    clave = (libro.genero, libro.titulo, libro.año)
    arbol_genero_titulo_año.insertar(clave, libro)

# Recorrido inorden del árbol por título y año
print("Recorrido inorden del árbol por título y año:")
arbol_titulo_año.inorden()

# Recorrido por nivel del árbol por género
print("\nRecorrido por nivel del árbol por género:")
arbol_genero_titulo_año.por_nivel()

# Mostrar información de libros específicos
print("\nInformación de libros específicos:")
print(arbol_titulo_año.buscar(("Cien años de soledad", 1967)).valor)
print(arbol_titulo_año.buscar(("1984", 1949)).valor)

# Mostrar libros del género "Ciencia Ficción"
print("\nLibros del género 'Ciencia Ficción':")
for libro in libros:
    if libro.genero == "Ciencia Ficción":
        print(libro)

# Listar libros con más de 500 páginas
print("\nLibros con más de 500 páginas:")
for libro in libros:
    if libro.paginas > 500:
        print(libro)

# Mostrar libros de la editorial "Planeta" o "Alfaguara"
print("\nLibros de la editorial 'Planeta' o 'Alfaguara':")
for libro in libros:
    if libro.editorial in ["Planeta", "Alfaguara"]:
        print(libro)  # No hay libros de estas editoriales en la lista

# Listar libros que comienzan con "E" o contienen ":"
print("\nLibros que comienzan con 'E' o contienen ':':")
for libro in libros:
    if libro.titulo.startswith("E") or ":" in libro.titulo:
        print(libro)

# Crear índice por autor
indice_autor = {}
for libro in libros:
    if libro.autor not in indice_autor:
        indice_autor[libro.autor] = []
    indice_autor[libro.autor].append(libro)

# Mostrar índice por autor
print("\nÍndice por autor:")
for autor, libros_autor in indice_autor.items():
    print(f"\nAutor: {autor}")
    for libro in libros_autor:
        print(libro.titulo)