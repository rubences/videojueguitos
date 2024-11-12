from Libro import Libro
from Arbol import Arbol

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

# Elimiar un libro del árbol por título y año
print("\nEliminando 'El nombre de la rosa' del árbol por título y año:")
arbol_titulo_año.eliminar(("El nombre de la rosa", 1980))
arbol_titulo_año.inorden()

# Modificar un libro del árbol por título y año
print("\nModificando 'El retrato de Dorian Gray' del árbol por título y año:")
arbol_titulo_año.modificar(("El retrato de Dorian Gray", 1890), "El retrato de Dorian Gray", 1891)
arbol_titulo_año.inorden()

# Mostrar libros con más de 500 páginas
print("\nLibros con más de 500 páginas:")
for libro in libros:
    if libro.paginas > 500:
        print(libro)

# Ordenar libros con postorden
print("\nOrdenar libros con postorden:")
arbol_titulo_año.postorden()

# Mostrar libros del género "Fantasía" o "Novela"
print("\nLibros del género 'Fantasía' o 'Novela':")
for libro in libros:
    if libro.genero in ["Fantasía", "Novela"]:
        print(libro)
        