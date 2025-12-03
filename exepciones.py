"""
lista = ["enero","febrero"]

print(lista[0])
print(lista[2])
"""

#num = int(input("Introduce un número: "))
"""
while True:
    try:     # Si puede dar error:
        num1=int(input("Introduce el dividendo: "))
        num2=int(input("Introduce el divisor: "))
        print(num1/num2)
    except ZeroDivisionError: # Dependiendo del tipo de error que se pueda producir:
        print("Operación no permitida. No se puede dividir entre 0.")
"""

while True:
    try:     # Si no se produce un error ejecuta todo esto y acaba
        num1=int(input("Introduce el dividendo: "))
        break
    except ValueError: # Si se produce el error se ejecuta esto
        print("Error. Debes introducir un número")


try:
    num1=int(input("Introduce el dividendo: "))
    num2=int(input("Introduce el divisor: "))
    print(f"La division de {num1} entre {num2} es {num1/num2}")
except ZeroDivisionError as e:
    print("No puedes dividr entre 0")
    print(e)
except ValueError as e:
    print("TIenes que introducir un número")
    print(e)
except:
    print("Error inesperado.")