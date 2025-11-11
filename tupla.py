# Tipos de datos compuestos

# listas
frutas = ["fresa","manzana","pera","piña"]
loteria = [10,25,30,40,50]
alumnos = []

print(frutas)
print(len(frutas))
print(len(loteria))
print(len(alumnos))

#Le añade a la lista temporalmente
frutas.append("plátano")
print(frutas)

# Añadir elementos de un segunda lista a la lista original
fruta_exotica = ["paraguayo","Mango","Fruta de dragon"]
frutas.extend(fruta_exotica)
print (frutas)

#Imprimir el elemento de una posición
print(frutas[0])
print(frutas[-1])
print(frutas[2:4])
print(frutas[::2])
print(frutas[::-1])

#Insertar un elemento en una posición
frutas.insert(1,"maracuyá")
print(frutas)

frutas[3]="kiwi"
print(frutas)

#Saber si tenemos un elemento en la lista
#comida=input("¿Que fruta quieres?: ")
#if comida in frutas:
#    print(f"Tenemos {comida}.")
#else:
#    print(f"No tenemos {comida}.")

#Eliminar elementos de una lista

del frutas[0]
print(frutas)

frutas.remove("paraguayo") # Elimina por nombre
print(frutas)

frutas.pop()