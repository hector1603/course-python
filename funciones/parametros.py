def datos(nombre, apellido, edad, mensaje):
    if edad < 18:
        print(f"{mensaje} {nombre} {apellido}, aun eres menor de edad.")
    else:
        print(f"{mensaje} {nombre} {apellido}, ya eres mayor de edad.")