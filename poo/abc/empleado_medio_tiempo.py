from empleado import Empleado

class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, salario_base, bono = 0.10):
        super().__init__(nombre, salario_base)
        self.bono = bono
    
    def calcular_salario(self):
        salario_final = self.salario_base + (self.salario_base * self.bono)
        return salario_final