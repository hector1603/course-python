import random

print("Bienvenido a Kraketravels, por favor elige tu destino: ")
print(" 1. Ecuador\n 2. Colombia\n 3. Perú")

destino = int(input("- "))

limites = {
    1: {  # Ecuador
        1: (10, 40),  # Urbana
        2: (41, 60),  # Rural
        3: (61, 80)   # Perimetral
    },
    2: {  # Colombia
        1: (10, 30),  # Urbana
        2: (31, 80),  # Rural
        3: (81, 100)  # Perimetral
    },
    3: {  # Perú
        1: (10, 40),  # Urbana
        2: (41, 60),  # Rural
        3: (61, 120)  # Perimetral
    }
}

# Verificar si el destino es válido
if destino in limites:
    print("****************** Destino Seleccionado ******************")
    print("Elija la zona:\n 1 - Urbana\n 2 - Rural\n 3 - Perimetral")
    zona = int(input("- "))

    # Verificar si la zona es válida
    if zona in limites[destino]:
        min_vel, max_vel = limites[destino][zona]

        while True:
            velocidad = random.randint(1, 121)

            if velocidad < min_vel:
                print(f"Velocidad {velocidad} km/h - Está por debajo del mínimo permitido ({min_vel} km/h).")
                break
            elif velocidad > max_vel:
                print(f"Velocidad {velocidad} km/h - Está por encima del máximo permitido ({max_vel} km/h).")
                break
            else:
                print(f"✅ Velocidad {velocidad} km/h - Respetando el límite de velocidad.")

    else:
        print("Opción de zona no válida.")
else:
    print("Opción de destino no válida.")
