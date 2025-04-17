class Libro:
    cantidad_libros = 0

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        Libro.cantidad_libros += 1

    def mostrar_info(self):
        print(f'Título: {self.titulo} \nAutor: {self.autor} \nPáginas: {self.paginas}')

    @staticmethod
    def es_grande(paginas):
        if paginas > 300:
            return True
        else:
            return False

    @classmethod   
    def total_libros(cls):
        print(f'Hay {cls.cantidad_libros} libros en la biblioteca.')