"""
Ejercicio 3
Crea un programa que pida tres números por teclado. 
El programa imprime en consola la media aritmética de los números introducidos
"""
def media():
    num1=int(input("Introduce el primer número: "))
    num2=int(input("Introduce el segundo número: "))
    num3=int(input("Introduce el tercer número: "))
    return ((num1+num2+num3)/(3))

print(f"La media aritmética es {media()}")