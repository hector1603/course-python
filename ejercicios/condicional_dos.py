import random

aleatorio = random.randint(1, 9)
alearotio_dos = random.randint(1, 9)

print("Primer número aleatorio: ", aleatorio)
print("Segundo número aleatoio: ", alearotio_dos)

if aleatorio == 7:
    print("Ganaste un chupete!")
elif alearotio_dos == 3:
    print("Ganaste una pelota!")
elif aleatorio == 5 and alearotio_dos == 8:
    print("Ganaste un televisor")
else: 
    print("No ganaste nada :(")