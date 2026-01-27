
lista_num = ["pollo","jaime","gato","perro"]
comp = []

def repetir(lista):
    for insertar in lista:
        if insertar not in comp:
            cont = 0
            comp.insert(cont,insertar)
            cont = cont +1 
        else:
            return True
    return False

resultado = (repetir(lista_num))

print(resultado)