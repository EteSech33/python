#Ejercicio 5
#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> 
# y un resto <r>, donde <n> y <m> son los números introducidos por el usuario, 
# y <c> y <r> son el cociente y el resto de la división entera respectivamente.

def numeritos():
    n = int(input("Introduce el primer numero entero: "))
    m = int(input("Introduce el segundo número entero: "))
    c = n/m
    r = n%m
    return n,m,c,r

n,m,c,r = numeritos()
print (f"La {n} entre {m} da un cociente de {c} y un resto de {r}")