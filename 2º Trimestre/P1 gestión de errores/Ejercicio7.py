def realizar_operacion(lista, indice):
    valor = lista[indice]
    resultado = 10 / valor
    return resultado

numeros = [2, 0, 5]
posicion = int(input("Introduce un índice de la lista: "))
resultado = realizar_operacion(numeros, posicion)
print(f"Resultado: {resultado}")
