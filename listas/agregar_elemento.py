# Agregar elementos a una lista

lista = [1, 2, 3, 4, 5]
lista.append(6)
lista.insert(2, "Hector")
lista.extend([7, 8, 9])

lista2 = [10, 11, 12]
lista3 = lista + lista2

print(lista3)