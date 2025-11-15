"""
Realizar un programa que comprueba si una cadena leída 
por teclado comienza por una subcadena introducida por teclado.
"""

cadena1=str(input("Escribe la subcadena: "))

cadena2=str(input("Escribe la cadena: "))

def palabra(cadena1,cadena2):
    if cadena1 in cadena2:
        print(f"{cadena1} es una cadena de {cadena2}.")
    else:
        print(f"{cadena2} y {cadena1} no son de la misma cadena.")

palabra(cadena1,cadena2)

