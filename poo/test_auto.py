from vehiculo import Vehiculo
from auto import Auto
from moto import Moto

lista_vehiculos = []

auto = Auto(5, 'Toyota', 'Corolla Cross', 2023)
moto = Moto('Deportiva', 'Bajaj', 'Rouser NS', 2025)

lista_vehiculos.append(auto)
lista_vehiculos.append(moto)

for vehiculos in lista_vehiculos:
    print(vehiculos.descripcion())