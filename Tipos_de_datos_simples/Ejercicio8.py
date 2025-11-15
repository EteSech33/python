"""
Ejercicio 8
Escribe un programa que solicite al usuario dos palabras, las cuales se guardarán en dos variables distintas. 
A continuación, almacena en otra variable la concatenación de la primera palabra, más un espacio, más la segunda palabra. 
Muestra este resultado en pantalla.
"""
def palabras():
    p1 = input("Introduce la primera palabra: ")
    p2 = input("Introduce la segunda palabra: ")
    p3 = p1 + " " + p2
    return p3

p3 = palabras()

print(p3)