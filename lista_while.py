regalos = ["reloj","ipad","playstation","xbox"]

for regalo in regalos:
    print(f"Quiero un/a {regalo}")

# Recorrer una lista con while
i = 0
while i<len(regalos):
    print(f"Quiero un/a {regalos[i]}")
    i+=1

# Recorrer en orden inverso con while
i = len(regalos)-1
while i>=0:
    print(f"Quiero un/a {regalos[i]}")
    i-=1


i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)


opcion=0
while opcion != 3:
    print("1. Opcion 1")
    print("2. Opcion 2")
    print("3. Salir")
    opcion=input("Introduce una opción")