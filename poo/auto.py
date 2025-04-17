from vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, numero_puertas, marca, modelo, anio):
        super().__init__(marca, modelo, anio)
        self.numero_puertas = numero_puertas
    
    def descripcion(self):
        descripcion_auto = super().descripcion()
        descripcion_auto += f' con {self.numero_puertas} puertas.'
        return descripcion_auto