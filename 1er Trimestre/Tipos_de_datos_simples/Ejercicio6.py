"""
Ejercicio 6
Escribe un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por en coche y 
la cantidad de litros de combustible que consumió durante ese recorrido. 
Mostrar el consumo del vehículo por cada 100 kilómetros recorridos.
"""
def solicitar():
    km = int(input("Introduce la cantidad de km recorridos en coche: "))
    L = int(input("Introduce la cantidad de litros de combustible que consumió durante ese recorrido: "))
    x = ((L * 100)/(km))
    return x

x = solicitar()

print(f"El coche consume {x} Litros cada 100km.")