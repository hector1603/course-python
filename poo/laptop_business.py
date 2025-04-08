from laptop import Laptop
import random

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria, almacenamiento, duracion_bateria, precio = 500, impuesto = 10):
        super().__init__(marca, procesador, memoria, precio, impuesto)
        self.almacenamiento = almacenamiento
        self.duracion_bateria = duracion_bateria

    def realizar_diagnostico_sistema(self):
        diagnostico =  super().realizar_diagnostico_sistema()
        diagnostico.update({
            "ALMACENAMIENTO": "Ok" if self.almacenamiento > 256 else "Espacio insuficiente"
        })

        return diagnostico
    
    def verificar_conectividad_red(self):
        conectividad = {
            "WiFi disponible": random.choice([True, False]),
            "Acceso a servidores empresariales": random.choice([True, False]),
            "Latencia de red aceptable": random.choice([True, False])
        }

        return conectividad