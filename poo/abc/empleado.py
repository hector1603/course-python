from abc import ABC, abstractmethod

class Empleado(ABC):

    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario(self):
        pass
