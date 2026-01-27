"""
Ejercicio 8
Escribe un programa que solicite al usuario dos palabras, las cuales se guardarán en dos variables distintas. 
A continuación, almacena en otra variable la concatenación de la primera palabra, más un espacio, más la segunda palabra. 
Muestra este resultado en pantalla.
"""
palabra1 = str(input("Introduce la primera palabra: "))
palabra2 = str(input("Introduce la segunda palabra: "))

palabra = palabra1 + " " + palabra2

print(f"La concatenación de {palabra1} y {palabra2} da como resultado {palabra}.")