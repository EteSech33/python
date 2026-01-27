# Gabriel Kirilov Chonov
"""
Crea un programa que muestre el siguiente menú de forma reiterada:
CAJERO ELECTRÓNICO BBVA
1- Ingresar efectivo
2- Retirada de efectivo
3- Mostrar movimientos
4- Salir
Selecciona una opción:
● Si se selecciona la opción 1, se preguntará al usuario la cantidad de dinero a
ingresar y se sumará al saldo del usuario. Además se añadirá el movimiento a una
lista llamada movimientos. Se informará al usuario del saldo disponible.
● Si se selecciona la opción 2, se preguntará cuánto dinero desea retirar y se
comprobará si el saldo del usuario es suficiente para realizar la operación. Si no lo
es, se mostrará un aviso y si es suficiente, se anotará el movimiento en la lista de
movimientos en negativo. Se informará al usuario del saldo disponible.
● Al seleccionar la opción 3 se mostrarán dos listas:
Ingresos [1000,200,50]
TOTAL INGRESADO: 1250€
Retiradas [-50,-300]
TOTAL RETIRADO: 350€
● Si se selecciona la opción 4 el programa finalizará
"""

saldo = 0
ingresar = 0
retirar = 0
suma_total_retirado = []
suma_total_ingresado = []
eleccion = 0
y = 0
z = 0

while eleccion != 4:
    
    print("CAJERO ELECTRÓNICO BBVA")
    print("1- Ingresar efectivo")
    print("2- Retirada de efectivo")
    print("3- Mostrar movimientos")
    print("4- Salir")
    
    eleccion = int(input("Introduce una opción número): "))
    
    if eleccion == 1: 
        print("\nVamos a ingresar efectivo.")
        ingresar = int(input("Ingresa la cantidad de dinero que quieres ingresar: "))
        saldo = saldo + ingresar
        suma_total_ingresado.append(saldo)

    elif eleccion == 2:
        print("2- Retirada de efectivo")
        retirar = int(input("Ingresa la cantidad de dinero que quieres retirar: "))
        if (retirar < saldo):
            saldo = saldo - retirar
            x = (retirar * -1)
            suma_total_retirado.append(x)
        else:
            print("Saldo insuficiente.")
    
    elif eleccion == 3:
        y = sum(suma_total_ingresado)
        z = sum(suma_total_retirado)
        
        print(f"TOTAL INGRESADO: {y} €")
        print(suma_total_ingresado)
        print(f"TOTAL RETIRADO: {z*-1} €")
        print(suma_total_retirado)

    elif eleccion == 4:
        print("Gracas por usar nuestro banco.")
    
    else:
        print("No has introducido ninguna opción válida")