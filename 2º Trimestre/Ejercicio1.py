import random

preguntas = [
    {
        'pregunta': '¿Cuál es la capital de Francia?',
        'respuestas': ['Madrid', 'París', 'Berlín', 'Lisboa'],
        'correcta': 1
    },
    {
        'pregunta': '¿Quién pintó la Mona Lisa?',
        'respuestas': ['Vincent van Gogh', 'Pablo Picasso', 'Leonardo da Vinci', 'Claude Monet'],
        'correcta': 2
    },
    {
        'pregunta': '¿Qué planeta está más cerca del Sol?',
        'respuestas': ['Venus', 'Mercurio', 'Marte', 'Tierra'],
        'correcta': 1
    },
    {
        'pregunta': '¿Cuál es el océano más grande?',
        'respuestas': ['Atlántico', 'Índico', 'Ártico', 'Pacífico'],
        'correcta': 3
    },
    {
        'pregunta': '¿En qué año llegó el hombre a la Luna?',
        'respuestas': ['1965', '1969', '1971', '1962'],
        'correcta': 1
    },
    {
        'pregunta': '¿Cuál es la capital de España?',
        'respuestas': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia'],
        'correcta': 0
    },
    {
        'pregunta': '¿Quién escribió "Cien años de soledad"?',
        'respuestas': ['Gabriel García Márquez', 'Mario Vargas Llosa', 'Pablo Neruda', 'Julio Cortázar'],
        'correcta': 0
    },
    {
        'pregunta': '¿Qué planeta es conocido como el "planeta rojo"?',
        'respuestas': ['Marte', 'Venus', 'Júpiter', 'Saturno'],
        'correcta': 0
    },
    {
        'pregunta': '¿Cuántos continentes hay en el mundo?',
        'respuestas': ['5', '6', '7', '8'],
        'correcta': 2
    },
    {
        'pregunta': '¿En qué año comenzó la Segunda Guerra Mundial?',
        'respuestas': ['1939', '1914', '1945', '1929'],
        'correcta': 0
    }
]

# Mezclar preguntas
random.shuffle(preguntas)

aciertos = 0

print("=== SABER Y GANAR ===\n")

for pregunta in preguntas:
    print(pregunta['pregunta'])
    
    # Mostrar opciones numeradas
    for num, opcion in enumerate(pregunta['respuestas']):
        print(f"{num}. {opcion}")
    
    # Pedir respuesta
    try:
        respuesta = int(input("Tu respuesta: "))
    except ValueError:
        print("Respuesta no válida. Fin del juego.")
        break

    # Comprobar acierto
    if respuesta == pregunta['correcta']:
        print("¡Correcto!\n")
        aciertos += 1
    else:
        print("Incorrecto. Fin del juego.\n")
        break

# Mostrar resultado final
print(f"Has acertado {aciertos} preguntas.")

# Calcular premio
if aciertos == 10:
    premio = 5000
elif aciertos == 9:
    premio = 2000
elif aciertos >= 7:
    premio = 1000
elif aciertos >= 4:
    premio = 500
else:
    premio = 0

print(f"Premio obtenido: {premio}€")
