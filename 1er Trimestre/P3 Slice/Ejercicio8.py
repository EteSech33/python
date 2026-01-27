"""
Realizar un programa que compruebe si una cadena contiene una subcadena. 
Las dos cadenas se introducen por teclado.
"""

cadena1=str(input("Escribe la cadena principal: "))

cadena2=str(input("Escribe la subcadena: "))

def palabra(cadena1,cadena2):
    if cadena2 in cadena1:
        print(f"{cadena2} es una subcadena de {cadena1}.")
    else:
        print(f"{cadena2} y {cadena1} no son de la misma cadena.")

palabra(cadena1,cadena2)
