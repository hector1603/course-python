frase = input("Ingrese una frase: ")
letra = input("Ingrese el caracter a buscar: ")

contador = 0
for i in frase:
    if letra == i:
        contador += 1
        
print(f"El caracter {letra} se repite {contador} veces")