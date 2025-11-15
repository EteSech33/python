"""
Ejercicio 8: Múltiplos
Crea un programa que pida dos números enteros al usuario (con input) y diga si alguno de ellos es múltiplo del otro. 
Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.
"""
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

def EsMultiplo(num1,num2):
    i = 0
    s = ""
    if (num1 % num2) == 0:
        s = f"{num1} es múltiplo de {num2}"
        return s
    else:
        s = f"{num1} no es múltiplo de {num2}"
        return s

s = EsMultiplo(num1,num2)

print(s)