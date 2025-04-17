from libro import Libro

lista_libros = []

libro1 = Libro('PADRE RICO PADRE POBRE', 'Robert Kiyosaki', 310)
libro2 = Libro('HABITOS ATOMICOS', 'James Clear', 213)
libro3 = Libro('TRAGUESE ESE SAPO', 'Brian Tracy', 212)

lista_libros.append(libro1)
lista_libros.append(libro2)
lista_libros.append(libro3)

for libro in lista_libros:
    libro.mostrar_info()
    print(f'Es un libro grande? {Libro.es_grande(libro.paginas)}\n')

Libro.total_libros()