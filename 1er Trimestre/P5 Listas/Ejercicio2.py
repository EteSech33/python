"""
Escribe una función llamada "elimina_repetidos" 
que reciba una lista y devuelva una nueva lista con los elementos únicos, 
sin repeticiones de la lista original. No tienen porqué estar en el mismo orden.
"""

lista = ["pollo","melon","pollo","pollo","boligrafo","pan","melon"]
lista_bien = []

def elimina_repetidos(lista,lista_bien):
    for elemento in lista:

        if elemento not in lista_bien: # Si el elemento de la lista no esta dentro lo añade.
            lista_bien.append(elemento)

    print(lista_bien) 
# Ponemos el print fuera del if, para que se imprima 
# cuando deje de comprobar que elementos hay en la lista


elimina_repetidos(lista,lista_bien)
