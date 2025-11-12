"""
Ejercicio 11: Área de un círculo y volumen de un cilindro.
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
"""

num1 = float(input("Introduce un el radio del círculo en cm: "))

def circulo(num1):
    if (num1 <= 0):
        print (f"Introduce un número mayore que 0.")
    else:
        a_circ = 3.1415 * (num1**2)
        print(f"El área del círculo es de {a_circ:.2f} centímetros") #Poner 2 decimales
        return a_circ

a_circ = circulo(num1)


alt = float(input("Introduce un la altura del cilindro en cm: "))

def volumen(a_circ,alt):
    if (alt <= 0):
        print (f"Introduce un número mayore que 0.")
    else:
        volumen = a_circ * alt
        print(f"El volumen del cilindro es de {volumen:.2f} centímetros") #Poner 2 decimales
        return volumen
    
volumen(alt,a_circ)
