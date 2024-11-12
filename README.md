# videojueguitos

## Desarrollo de índices mediante árboles ordenados de búsqueda

Dada una lista de instancias de la clase Videojuego, que cuentan con: título, género, año de lanzamiento, duración, clasificación (E, T, M) y desarrollador, los últimos tres atributos pueden tener más de un valor. 

Escribir las funciones necesarias para resolver las siguientes cuestiones:

### a. Definir la clase Videojuego con su constructor;

b. Crear dos árboles de acceso a los datos, definiendo la clase Árbol, clasificados:

por título y año
por clasificación, título y año;

c. Realizar un recorrido inorden del árbol por título y año de lanzamiento;

d. Realizar un recorrido por nivel de los árboles por clasificación;

e. Mostrar toda la información de "The Legend of Zelda: Breath of the Wild" y "The Witcher 3: Wild Hunt";

f. Mostrar todos los videojuegos con clasificación “M”;

g. Listar todos los videojuegos que tienen una duración mayor a 50 horas;

h. Mostrar todos los videojuegos del género “Acción” o “Aventura”;

i. Listar los videojuegos que comienzan con la letra “S” y los que contienen un “:” en su título;

j. Crear un índice por género, que contenga para cada nodo del árbol el género y la lista de todos los videojuegos con el mismo.

La lista de videojuegos puede ser la siguiente:

Lista de videojuegos
Python
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




# Desarrollo de índices mediante árboles ordenados de búsqueda


Dada una lista de instancias de la clase Libro, que cuentan con: título, autor, año de publicación, número de páginas, género (Novela, Ciencia Ficción, Fantasía, Biografía, etc.)  y editorial. Escribir las funciones necesarias para resolver las siguientes cuestiones:

a. Definir la clase Libro con su constructor;

b. Crear dos árboles de acceso a los datos, definiendo la clase Árbol, clasificados:

por título y año de publicación
por género, título y año de publicación;
c. Realizar un recorrido inorden del árbol por título y año de publicación;

d. Realizar un recorrido por nivel de los árboles por género;

e. Mostrar toda la información de "Cien años de soledad" y "1984";

f. Mostrar todos los libros del género “Ciencia Ficción”;

g. Listar todos los libros que tienen más de 500 páginas;

h. Mostrar todos los libros de la editorial “Planeta” o “Alfaguara”;

i. Listar los libros que comienzan con la letra “E” y los que contienen un “:” en su título.

j. Crear un índice por autor, que contenga para cada nodo del árbol el autor y la lista de todos los libros con el mismo autor.

La lista de libros puede ser la siguiente:

Python
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
