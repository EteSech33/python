"""
Ejercicio 6
Escribe un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por en coche y 
la cantidad de litros de combustible que consumió durante ese recorrido. 
Mostrar el consumo del vehículo por cada 100 kilómetros recorridos.
"""
def solicitar():
    km = int(input("Introduce la cantidad de km recorridos en coche: "))
    L = int(input("Introduce la cantidad de litros de combustible que consumió durante ese recorrido: "))
    x = (km*100)/(L)
    return x
print(f"El coche gasta {solicitar()} litros por cada 100km.")