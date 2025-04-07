class Auto:
    def __init__(self, marca, modelo, año, kilometraje = 0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

    def mostrar_informacion(self):
        print(f'El auto es un {self.marca} modelo {self.modelo} del {self.año}')

    def actualizar_kilometraje(self, kilometraje):
        if kilometraje < self.kilometraje:
            print('No se puede reducir el kilometraje')
        else:
            self.kilometraje = kilometraje

    def realizar_viaje(self, kilometros):
        if kilometros > 0:
            self.kilometraje += kilometros
        else:
            print('La cantidad de kilometros debe ser positivo')
    
    def estado_auto(self):
        if self.kilometraje < 20000:
            print('🟢 Estoy como nuevo')
        elif self.kilometraje >= 20000 and self.kilometraje <= 100000:
            print('🟡 Ya estoy usado')
        else:
            print('🔴 Ya dejame descansar por favor!')


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