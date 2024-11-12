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