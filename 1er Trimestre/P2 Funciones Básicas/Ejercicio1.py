"""
Ejercicio 1: Saludo
Crea una función que reciba dos parámetros. 
El primero será el saludo y el segundo será la persona a la que va dirigido el saludo. 
Deberá imprimir por pantalla el saludo correspondiente. 
Invoca la función para comprobar su funcionamiento.
"""
def saludar():
    saludo = input("Escribe el saludo: ")
    persona = input ("Escribe el nombre a la que va dirigido el saludo: ")
    return saludo, persona

saludo, persona = saludar()

print(saludo, persona)