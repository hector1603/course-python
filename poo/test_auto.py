from auto import Auto

auto1 = Auto.toyota_actual('Cross')
auto2 = Auto('Toyota', 'Yaris', '2020', 0)
auto3 = Auto.auto_usado()

auto1.mostrar_informacion()
auto2.mostrar_informacion()

if Auto.mismo_kilometraje(auto1, auto3):
    print('Ambos autos tienen el mismo kilometraje.')
else:
    print('Los autos tienen kilometrajes diferentes.')

auto_mas_km = Auto.auto_con_mas_kilometraje(auto2, auto3)
print('El auto con más kilometraje es:')
auto_mas_km.mostrar_informacion()

auto = None

while True:
    print("\n===== MENÚ DE AUTO =====")
    print("1. Crear auto")
    print("2. Mostrar información del auto")
    print("3. Actualizar kilometraje")
    print("4. Realizar viaje")
    print("5. Ver estado del auto")
    print("0. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        año = input("Año: ")
        try:
            kilometraje = int(input("Kilometraje inicial (opcional - Enter para 0): ") or 0)
            auto = Auto(marca, modelo, año, kilometraje)
            print("✅ Auto creado con éxito.")
        except ValueError:
            print("⚠️ Kilometraje inválido.")

    elif opcion == "2":
        if auto:
            auto.mostrar_informacion()
        else:
            print("⚠️ Primero debes crear un auto.")

    elif opcion == "3":
        if auto:
            try:
                nuevo_km = int(input("Nuevo kilometraje: "))
                auto.actualizar_kilometraje(nuevo_km)
            except ValueError:
                print("⚠️ Ingresa un número válido.")
        else:
            print("⚠️ Primero debes crear un auto.")

    elif opcion == "4":
        if auto:
            try:
                km_viaje = int(input("¿Cuántos km fue el viaje?: "))
                auto.realizar_viaje(km_viaje)
            except ValueError:
                print("⚠️ Ingresa un número válido.")
        else:
            print("⚠️ Primero debes crear un auto.")

    elif opcion == "5":
        if auto:
            print(auto.estado_auto())
        else:
            print("⚠️ Primero debes crear un auto.")

    elif opcion == "0":
        print("👋 Saliendo del sistema. ¡Hasta luego!")
        break

    else:
        print("⚠️ Opción no válida. Intenta de nuevo.")