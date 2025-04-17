from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, tipo, marca, modelo, anio):
        super().__init__(marca, modelo, anio)
        self.tipo = tipo
    

    def descripicon(self):
        descripcion_moto = super().descripcion()
        descripcion_moto += f' del tipo {self.tipo}.'
        return descripcion_moto