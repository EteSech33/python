# Gabriel Kirilov Chonov
"""
Realiza un programa que solicite al usuario que introduzca una frase y cuente cuántas
vocales hay en ella. El programa debe contar tanto las vocales minúsculas como las
mayúsculas. Deberás utilizar listas para resolver el ejercicio.
"""

frase= str(input("Introduce una frase para contar sus vocales: "))
i = 0
vocales = ["a","e","i","o","u","A","E","I","O","U"]

for letras in frase:
    if letras in vocales:
        i+=1

print(f"{frase} tiene {i} vocales.")

