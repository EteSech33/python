def pollo():
    print("pollo")

pollo()

def mensaje():
    return "HOla que tal"


mensj = mensaje()
print(mensj)
"""
La función mensaje va a devolver el return en la variable mensj
"""

#Función suma
"""
def suma(num1,num2):
    resultado = num1 + num2
    return resultado

res1 = suma(1,1)
res2 = suma(2,2)
print(res1,res2)
"""

def sumar_v2():
    num1=int(input("Introduce el primer número: "))
    num2=int(input("Introduce el primer número: "))
    resultado = num1 + num2
    return num1 + num2

print (f"El numerito es {sumar_v2()}")

