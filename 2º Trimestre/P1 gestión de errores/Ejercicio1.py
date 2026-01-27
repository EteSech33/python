lista = [1, 2, 3, 4, 5]

try:
    indice = int(input("Introduce un índice para acceder a la lista: "))
    print(f"El valor en la posición {indice} es: {lista[indice]}")
except IndexError:
        print("Has introducido un índice no válido.")