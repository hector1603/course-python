nota_tarea = float(input("Ingrese la nota de la tarea: "))
nota_leccion = float(input("Ingrese la nota de la lección: "))
nota_examem = float(input("Ingrese la nota del examen: "))

promedio = (nota_tarea + nota_leccion + nota_examem) / 3

print(f"El promedio de las notas es: {promedio}")