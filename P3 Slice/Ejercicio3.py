"""
Crear un programa en Python que solicite al usuario el precio de un producto. 
El programa mostrará por pantalla un mensaje informando del total de euros y céntimos en esa cantidad.
Ejemplo: 
Introduce un precio: 25.75
El importe total es de 25 euros y 75 céntimos de euro.
"""

precio = input(str("Introduce el precio de tu producto (solo la cantidad): "))

def calcular(precio):
    
    cantidad = precio.find(".")

    euro = precio[:cantidad] #Del punto hasta la izquierda
    cent = precio[cantidad+1:] #Del punto hasta la derecha, quitando el punto

    return euro,cent

euro, cent = calcular(precio)

print(f"El importe total es de {euro} euros y {cent} céntimos de euro.")
    