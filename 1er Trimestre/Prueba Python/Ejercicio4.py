"""
Realiza una función que reciba un valor en binario (una cadena de texto) y devuelva el
número en decimal. Invoca a la función y utilizando el resultado imprime el mensaje “El
número binario X es en decimal Y”.
PISTA: Deberás dar la vuelta a la cadena de texto. Una vez al revés, deberás elevar 2 a la
posición en la que está el número y acumular la cantidad sólo si hay un 1 en la posición.
Ejemplo de ejecución:
Introduce un número binario: 1010101001010101
# Llamada a la función aquí.
El número binario 1010101001010101 es en decimal 43605
"""

num = int(input("Introduce el número en binario): "))
num_bin = list(str(num))
print(len(num_bin))
lista=[]

elevado=len(num_bin)

i=0

for numero in num_bin:
    
    x = (int(numero)*2)**(elevado)
    lista.append(x)
    i+=1
    elevado - i

print(sum(lista))
