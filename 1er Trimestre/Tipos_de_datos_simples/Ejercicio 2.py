#Ejercicio 2
"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde. 
"""
def trabajar():
    horas=float(input("¿Cuántas horas has trabajado? Introduce solo las horas: "))
    precio=float(input("¿Cuánto es el precio por hora? Introduce solo el número: "))
    return horas * precio

print(f"Chacho te van a dar {trabajar()}€2")