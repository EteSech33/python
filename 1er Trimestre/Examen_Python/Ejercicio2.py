
lista = [4,5,6,7,8,9,1]
lista_umbral = []

def filtrar_lista(lista,umbral):
    for numeros in lista:
        if numeros > umbral:
            cont = 0
            lista_umbral.insert(cont,numeros)
            cont = cont+1
    lista_umbral.sort()
    return lista_umbral

resultado = filtrar_lista(lista,5)

print(resultado)
