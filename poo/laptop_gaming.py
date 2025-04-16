from laptop import Laptop

class Laptop_Gaming(Laptop):
    def __init__(self, marca, procesador, memoria, tarjeta_grafica, precio=500, impuesto=10):
        super().__init__(marca, procesador, memoria, precio, impuesto)
        self.tarjeta_grafica = tarjeta_grafica

    def __str__(self):
        return f" Marca: {self.marca}\n Procesador: {self.procesador}\n Memoria: {self.memoria}\n Tarjeta grafica: {self.tarjeta_grafica}\n Precio: {self.precio}\n Impuesto: {self.impuesto}"

    def realizar_diagnostico_sistema(self):
        resultado_diagnostico =  super().realizar_diagnostico_sistema()
        resultado_juegos = self.realizar_diagnostico_juegos()
        resultado_diagnostico["Resultado juegos"] = resultado_juegos
        return resultado_diagnostico
    
    def realizar_diagnostico_juegos(self):
        juegos = ['FORNITE', 'COD', 'GTA']
        resultado = {}
        for juego in juegos:
            fps_base = 30
            if 'RTX' in self.tarjeta_grafica:
                fps = fps_base * 3
            elif 'GTX' in self.tarjeta_grafica:
                fps = fps_base * 2
            else:
                fps = fps_base
        
            resultado[juego] = f'{fps} FPS'

        return resultado

    def realizar_informe_uso(self):
        informe = super().realizar_informe_uso()
        informe.update({
            "Tipo": 'Gaming',
            "Uso recomendado": 'Juegos de video',
            "Horas de uso": 10,
            "Recomendaciones de software": ['Antivirus', 'VPN']
        })
    
        return informe