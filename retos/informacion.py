import datetime

fecha_actual = datetime.datetime.now()
anio_actual = fecha_actual.year

print(anio_actual)

nombre_paciente = []
anio_paciente = []
edad_paciente = []

def agregar_nombre(nombre):
    nombre_paciente.append(nombre)

def agregar_edad(anio_nacimiento):
    anio_paciente.append(anio_nacimiento)
    edad = anio_actual - anio_nacimiento
    edad_paciente.append(edad)

def mostrar_pacientes():
    if(len(nombre_paciente) == 0 and len(edad_paciente) == 0):
        print("No hay pacientes registrados")
    else:
        print(f"{nombre_paciente}\n{edad_paciente}")
        print(f"El paciente con mayor edad tiene {max(edad_paciente)} años.")
        print(f"El paciente mas menor tiene {min(edad_paciente)} años.")

