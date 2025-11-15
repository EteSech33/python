"""
Ejercicio 7: Mayor de edad
Crea una función llamada es_mayor_de_edad, 
que reciba un número que represente la edad de una persona y devuelva True si la persona es mayor de edad (18 años o más), y False si no lo es.

Pide al usuario su edad con un input, conviértelo a entero. 
Invoca la función anterior y si la persona es mayor de edad deberás decirle “Eres mayor de edad, 
puedes matricularte para sacarte el carnet de conducir”.
"""

edad = int(input("Introduce tu edad: "))

def es_mayor_edad(edad):
    if (edad < 18):
        return False
    else:
        return True

print (es_mayor_edad(edad))
