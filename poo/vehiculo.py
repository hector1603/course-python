class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        
    def descripcion(self):
        return f'Este vehiculo es un {self.marca} {self.modelo} del año {self.anio}'