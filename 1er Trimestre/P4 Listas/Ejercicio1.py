"""
Crea una función is_empty que reciba una lista y devuelva True si la lista está vacía o False si no lo está.
Ejemplo:
lista_vacia = []
print(is_empty(lista_vacia))
# El resultado será True
"""

lista = ["pollo"]

def is_empty(lista):
    if len(lista) != 0:
        return False
    else:
        return True

print(is_empty(lista))
