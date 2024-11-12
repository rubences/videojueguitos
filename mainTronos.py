from Arbol import Arbol
from Personajes import Personaje



# Lista de personajes
personajes = [
    Personaje("Daenerys Targaryen", "Targaryen", 25, "vivo", "femenino", "Reina"),
    Personaje("Jon Snow", "Stark", 28, "vivo", "masculino", "Rey"),
    Personaje("Tyrion Lannister", "Lannister", 40, "vivo", "masculino", "Mano de la Reina"),
    Personaje("Cersei Lannister", "Lannister", 42, "muerto", "femenino", "Reina"),
    Personaje("Arya Stark", "Stark", 18, "vivo", "femenino", "Ninguno"),
    Personaje("Sansa Stark", "Stark", 20, "vivo", "femenino", "Lady de Winterfell"),
    Personaje("Jaime Lannister", "Lannister", 42, "muerto", "masculino", "Lord Comandante de la Guardia Real"),
    Personaje("Bran Stark", "Stark", 16, "vivo", "masculino", "Rey de los Seis Reinos"), 
    Personaje("Theon Greyjoy", "Greyjoy", 26, "muerto", "masculino", "Príncipe de las Islas de Hierro")
]

# Crear el árbol por nombre y edad
arbol_nombre_edad = Arbol()
# Insertar personajes en el árbol por nombre y edad
for personaje in personajes:
    clave = (personaje.nombre, personaje.edad)
    arbol_nombre_edad.insertar(clave, personaje)

# Crear el árbol por casa, nombre y edad
arbol_casa_nombre_edad = Arbol()
# Insertar personajes en el árbol por casa, nombre y edad
for personaje in personajes:
    clave = (personaje.casa, personaje.nombre, personaje.edad)
    arbol_casa_nombre_edad.insertar(clave, personaje)

# Recorrido inorden del árbol por nombre y edad
print("Recorrido inorden por nombre y edad:")
inorden_result = arbol_nombre_edad.inorden()
if inorden_result:
    for clave, personaje in inorden_result:
        print(personaje.nombre, personaje.edad)
else:
    print("El árbol está vacío o la función inorden no está implementada correctamente.")

# Recorrido por nivel del árbol por casa
print("\nRecorrido por nivel por casa:")
por_nivel_result = arbol_casa_nombre_edad.por_nivel()
if por_nivel_result:
    for clave, personaje in por_nivel_result:
        print(personaje.casa, personaje.nombre, personaje.edad)
else:
    print("El árbol está vacío o la función por_nivel no está implementada correctamente.")

# Mostrar información de "Daenerys Targaryen" y "Jon Snow"
print("\nInformación de Daenerys Targaryen y Jon Snow:")
for personaje in personajes:
    if personaje.nombre in ["Daenerys Targaryen", "Jon Snow"]:
        print(vars(personaje))

# Mostrar todos los personajes de la casa “Stark”
print("\nPersonajes de la casa Stark:")
for personaje in personajes:
    if personaje.casa == "Stark":
        print(personaje.nombre)

# Listar todos los personajes que tienen más de 30 años
print("\nPersonajes con más de 30 años:")
for personaje in personajes:
    if personaje.edad > 30:
        print(personaje.nombre)

# Mostrar todos los personajes con estatus “vivo”
print("\nPersonajes vivos:")
for personaje in personajes:
    if personaje.estatus == "vivo":
        print(personaje.nombre)

# Listar los personajes que comienzan con la letra “A” y los que tienen un título que contiene la palabra “Rey”
print("\nPersonajes que comienzan con la letra 'A':")
for personaje in personajes:
    if personaje.nombre.startswith("A"):
        print(personaje.nombre)

print("\nPersonajes con título que contiene la palabra 'Rey':")
for personaje in personajes:
    if "Rey" in personaje.titulo:
        print(personaje.nombre)

# Crear un índice por género
indice_genero = {}
for personaje in personajes:
    if personaje.genero not in indice_genero:
        indice_genero[personaje.genero] = []
    indice_genero[personaje.genero].append(personaje)

print("\nÍndice por género:")
for genero, lista_personajes in indice_genero.items():
    print(f"{genero}: {[personaje.nombre for personaje in lista_personajes]}")