# Gabriel Kirilov Chonov
"""
Crea un programa que comprobará si tu boleto de la lotería es ganador. El programa
almacenará en memoria el boleto ganador (en una tupla), por ejemplo:
boleto_ganador=(9,23,67,56,4)
El programa deberá solicitar al usuario 5 números. Deberás utilizar range para resolver el
ejercicio. Si todos los números introducidos por el usuario se encuentran en el boleto
ganador, deberás mostrar el mensaje “GANASTE”.
Si no, deberás indicar el número de aciertos y mostrar el mensaje “MÁS SUERTE PARA LA
PRÓXIMA”
"""

boleto_ganador=(9,23,67,56,4)

print("Introduce 5 números: ")
numero1 = int(input("Introduce el 1er número: "))
numero2 = int(input("Introduce el 2º número: "))
numero3 = int(input("Introduce el 3er número: "))
numero4 = int(input("Introduce el 4º número: "))
numero5 = int(input("Introduce el 5º número: "))

numeros_usuario = [numero1, numero2, numero3, numero4, numero5]

if numeros_usuario == boleto_ganador:
    print("Has ganado.")

