"""
Ejercicio 4:  Longitud de una cadena de texto.
Crea una función que reciba un nombre e imprima un mensaje diciendo el número de caracteres que contiene la función.
"""

def longitud():
    palabra = str(input("Dime la palabra de la que quieras tener la longitud: "))

    cantidad = len(palabra)

    print(f"{palabra} tiene un total de {cantidad} de carácteres.")

longitud()