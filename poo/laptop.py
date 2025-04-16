import random

class Laptop:
    def __init__(self, marca, procesador, memoria, precio = 500, impuesto = 10):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.precio = precio
        self.impuesto = impuesto

    def valor_final(self):
        return self.precio + self.impuesto
    
    def valor_descuento(self, descuento):
        return (self.precio * descuento) / 100
    
    def realizar_diagnostico_sistema(self):
        resultado = {
            "MARCA": f"{self.marca}",
            "PROCESADOR": f"{self.procesador}",
            "RAM": 'Ok' if self.memoria >= 8 else 'Aumentar memoria RAM',
            "BATERIA": 'Ok' if random.choice([True, False]) else 'Cambiar de bateria'
        }

        return resultado

    def realizar_informe_uso(self):
        resultado_informe = {
            "Tipo": 'Generico',
            "Uso recomendado": 'Tareas cotidianas',
            "Horas de uso": 5,
            "Diagnostico actual": self.realizar_diagnostico_sistema()
        }

        return resultado_informe