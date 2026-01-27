"""
Ejercicio 13: División
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error indicando “No es posible dividir entre 0”
"""

num1 = int(input("Escriba el primer numero que será dividido: "))
num2 = int(input("Escriba el segundo numero para dividir: "))

def dividir(num1,num2):
    if (num1 == 0):
        print ("No es posible dividir entre cero.")
        return None
    else:
        return num1/num2

div = dividir(num1,num2)

if (div != None):
    print (f"Has dividido {num1}/{num2} y el resultado es {div}.")
