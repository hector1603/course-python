from datetime import datetime

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

    @classmethod
    def toyota_actual(cls, modelo):
        anio_actual = datetime.now().year
        return cls('Toyota', modelo, anio_actual)
    
    @staticmethod
    def mismo_kilometraje(auto1, auto2):
        return auto1.kilometraje == auto2.kilometraje
    
    @classmethod
    def auto_usado(cls):
        return cls('Nissan', 'Sentra', 2015, 8500)
    
    @staticmethod
    def auto_con_mas_kilometraje(auto1, auto2):
        if auto1.kilometraje > auto2.kilometraje:
            return auto1
        return auto2

