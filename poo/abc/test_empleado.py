from empleado import Empleado
from empleado_tiempo_completo import EmpleadoTiempoCompleto
from empleado_medio_tiempo import EmpleadoMedioTiempo

empleados = []

empleado_tc = EmpleadoTiempoCompleto('Hector', 2000.0)
empleado_mt = EmpleadoMedioTiempo('Lucas', 1000.0)

print(empleado_tc.calcular_salario())
print(empleado_mt.calcular_salario())

empleados.append(empleado_tc)
empleados.append(empleado_mt)

print('\n======== Calculo de salario final ========')
for empleado in empleados:
    print(f'{empleado.nombre} {empleado.calcular_salario():.2f}')
