def obtener_numero():
    while True:
        try:
            return int(input("Introduce un número entero: "))
        except ValueError:
            print("No has introducido un valor válido.")

numero = obtener_numero()
print(f"El número introducido es: {numero}")


"""
Modifica el programa para que siga pidiendo al usuario 
un número hasta que introduzca una entrada válida. 
Utiliza un bucle con manejo de excepciones.
"""