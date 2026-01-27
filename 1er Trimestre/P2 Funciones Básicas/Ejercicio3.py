"""
Ejercicio 3: Número par o impar
Crear una función que nos diga si un número es par o impar.
"""
def numeros():
    num = int(input("Ingresa tu número: "))

    if ((num % 2) == 0):
        print(f"El número {num} es par.")
    else:
        print(f"El número {num} es impar.")

numeros()
