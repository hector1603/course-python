#Calcular el area, perimetro y la superficie de un rectangulo.

base = float(input("Ingrese la base del rectangulo: A = "))
altura = float(input("Ingrese la altura del rectangulo: H = " ))

area = base * altura
perimetro = 2 * (base + altura)
superficie = base * altura

print("")
print(f"El area del rectangulo es: {area}")
print(f"El perimetro del rectangulo es: {perimetro}")
print(f"La superficie del rectangulo es tambien el area: {superficie}")