edades = {
    "Ana": 25,
    "Juan": 30,
    "Luis": 28
}

while True:
    try:
        nombre = input("Introduce un nombre para obtener la edad: ")
        print(f"La edad de {nombre} es: {edades[nombre]}")
    except KeyError:
        print("Has introducido un nombre no válido.")
