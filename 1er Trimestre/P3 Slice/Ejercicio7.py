"""
Introducir una cadena de caracteres e indicar si es un palíndromo. 
Una palabra palíndroma es aquella que se lee igual adelante que atrás.
"""

def palindroma(palabra):
    if palabra == palabra[::-1]:
        print(f"{palabra} es un palindromo.")
    else:
        print(f"{palabra} NO es un palindromo.")

palindroma("paap")