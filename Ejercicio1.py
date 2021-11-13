class Libro:
    def __init__(self, titulo, genero, num_paginas, autor):
        self.titulo = titulo
        self.genero = genero
        self.num_paginas = num_paginas
        self.autor = autor
    
    def book_details(self):
        print("Libro:", self.titulo)
        print("Autor:", self.autor)
        print("Genero:", self.genero)
        print("Numero de paginas:", self.num_paginas)
    
libros_leidos = []

def add_libro():
    libro = Libro(input("Introduce el nombre del libro que has leido: "), input("Genereo al que pertenece el libro: "), int(input("Numero de paginas: ")),
    input("Autor del libro: "))
    libros_leidos.append(libro)

def consultarLibrosLeidos():
    for libros in libros_leidos:
        libros.book_details()

for i in range(3):
    add_libro()

consultarLibrosLeidos()