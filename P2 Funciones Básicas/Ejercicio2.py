"""
Ejercicio 2: Tipo de una variable
Crea una función que reciba una variable y nos diga cuál es su tipo.
"""

def tipo(variable):
    x = type(variable)
    return x

x = tipo(2)
print(x)
