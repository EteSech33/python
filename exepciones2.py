"""
colores = {'rojo':'red','azul':'blue'}
color = input("Introduce un color: ")
print(f"El color {color} en ingles es {colores[color]}")
"""

def agregar_una_vez(lista,elemento):
    if elemento not in lista:
        lista.append(elemento)
    else:
        #Voy a generar una exepción
        raise ValueError("Elementos duplicados")

# Ejecución de la función
lista = ["tomate","pimineto","cebolla"]
agregar_una_vez(lista,"alcachofa")
try:
    agregar_una_vez(lista,"tomtate")
except ValueError:
    print("ERROR: Imposible añadir elementos duplicados")

print(lista)