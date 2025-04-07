lista = [1, 2, 3, 4, 5, "Hector", 6, 6, 6, "Hector", 7, 8, 9]

lista.pop() # Elimina el ultimo elemento de la lista
lista.remove(6) # Elimina un elemento segunla posicion del indice
lista.remove("Hector") # Elimina el elmento especificado

lista.clear() # Elimina todos los elementos de la lista

print(lista)

nueva_lista = [9, 7, 6, 5, 4, 2, 8]

#nueva_lista.sort() # Ordena los elementos de la lista de menor a mayor
nueva_lista.reverse() # INvierte los elementos de la lista
nueva_lista.sort(reverse = True) # Ordena los elementos de la lista de forma descendente

print(nueva_lista)