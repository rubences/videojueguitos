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
