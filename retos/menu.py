opcion = -1
menu = []

while opcion != 0:
    print("****** Segunda es Todo ******")
    print("Seleccione la operación a realizar.")
    print("1. Añadir plato al menú \n2. Buscar en el menú \n3. Eliminar plato del menú \n4. Mostrar platos del menú")
    print("0. Salir")

    opcion = int(input("Opción: "))

    if opcion == 1:
        plato = input("Ingrese el plato a agregar: ")
        menu.append(plato)
    elif opcion == 2:
        plato = input("Ingrese el plato a buscar: ")
        if plato in menu:
            print("El plato se encuentra en el menú")
        else:
            print("El plato no se encuentra en el menú")
    elif opcion == 3:
        plato = input("Ingrese el plato a eliminar: ")
        if plato in menu:
            menu.remove(plato)
        else:
            print("El plato no se encuentra en el menú")
    elif opcion == 4:
        print(f"Platos del menú: {menu}")
    elif opcion == 0:
            print("Gracias por usar el programa. ¡Hasta pronto!")
    else:
        print("Opción no válida")
        