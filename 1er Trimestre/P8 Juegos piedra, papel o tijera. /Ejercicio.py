import random

opciones = ["Piedra","Papel","Tijera"]
eleccion = "Y"
pc =""
jugador =""

while eleccion != "N":
    pc = random.choice(opciones)
    jugador = str(input("Introduce tu opción: ")).lower().capitalize()

    if jugador == pc:
        print("¡Has empatado!")
    elif ((jugador == "Piedra") and (pc == "Tijera")):
        print(f"¡Has ganado! Has sacado {jugador} y la máquina {pc}.")
    elif ((jugador == "Papel") and (pc == "Piedra")):
        print(f"¡Has ganado! Has sacado {jugador} y la máquina {pc}.")
    elif ((jugador == "Tijera") and (pc == "Papel")):
        print(f"¡Has ganado! Has sacado {jugador} y la máquina {pc}.")
    else:
        print(f"¡Has perdido! Has sacado {jugador} y la máquina {pc}.")
    
    eleccion = str(input("¿Quieres jugar de nuevo? (S/N): ")).lower().capitalize()

print("¡Gracias por jugar! Adiós.")

