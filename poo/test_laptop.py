from laptop_gaming import Laptop_Gaming
from laptop_business import Laptop_Business

laptop1 = Laptop_Gaming('Dell', 'i9', 4, 'RTX 8GB')
laptop_empresarial = Laptop_Business(
    marca="Dell",
    procesador="Intel i7",
    memoria=16,
    almacenamiento=512,
    duracion_bateria="8 horas"
)

print('------------------ Diagnóstico del sistema ------------------')
print(laptop_empresarial.realizar_diagnostico_sistema())
print('------------------ Diagnóstico de conectividad ------------------')
print(laptop_empresarial.verificar_conectividad_red())

#print(laptop1.realizar_diagnostico_sistema())