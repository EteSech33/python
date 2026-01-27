"""
La función min(lista) devuelve el valor más pequeño contenido en una lista. 
Crea una función que devuelva el número más pequeño en una lista de números. 
Hazlo con bucle for sin utilizar la función min.
"""

lista = [21,2,81,23,55,72,19,43,66]
numer = lista[0]

def min(lista,numer):
    for numeros in lista:
        if numeros < numer:
            numer = numeros 
            print(f"El numero más bajo es {numer}")

min(lista,numer)
