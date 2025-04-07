datos = []
frase = input("Ingrese los datos que decee: ")

entero = 0
cadena = 0
for caracter in frase:
    if caracter.isdigit():
        datos.append(caracter)
        entero += 1
    elif caracter.isalpha():
        datos.append(caracter)
        cadena += 1

print(f"Su lista es: {datos}\n Números:  {entero}\n Cadenas: {cadena}")