import informacion

opcion = -1

def agregar_informacion():
    nombre = input("Ingrese el nombre del paciente: ")
    anio = int(input("Ingrese el año de nacimiento: "))
    informacion.agregar_nombre(nombre)
    informacion.agregar_edad(anio)

while opcion != 0:
    print("*********** REGISTRO DE PACIENTES ***********")
    print("1. Registrar paciente\n0. Salir")

    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        agregar_informacion()
        print("Paciente agregado con éxito")
    elif opcion == 0:
        print("Hasta luego")
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

informacion.mostrar_pacientes()