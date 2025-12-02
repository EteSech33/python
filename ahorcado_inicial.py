import random

AHORCADO = [
    r'''
       +---+
       |   |
           |
           |
           |
           |
    =========''', r'''
       +---+
       |   |
       O   |
           |
           |
           |
    =========''', r'''
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========''', r'''
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========''', r'''
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========''', r'''
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========''', r'''
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    ========='''
]

numero = 0
cont = 0
adivinar = []
palabra = []
z = 0

# Elige una palabra de forma aleatoria y calcula su longitud y la convierte en rusta
def get_palabra_secreta():
      palabras = ["casa"] #,"coche","tomate","lechuga"
      x = random.choice(palabras)
      y = len(x)
      palabra = list(x)
      return x,y,palabra

x,y,palabra = get_palabra_secreta()

# Imprime la posicion de la horca que tenga el contador, si fallas el contador sube
def print_horca(cont):
      print(AHORCADO[cont])

# Con la longitud de la palabra secreta hace una lista exacta de longitud pero con guiones
def guiones(z,y):
      while (z != y):
            adivinar.append("-")
            z = z + 1 
guiones(z,y)

# Mientras que el contador sea menor que 6 se hace todo
while (cont <= 6):

      print_horca(cont)

      letra_usuario = str(input("Introduce una letra para adivinar: "))
      pos=0
      for letra in palabra: #Por cada letra en la palabra secreta, comprueba que si la letra del usuario es la letra de la palabra secreta
            if letra_usuario == letra:
                  adivinar[pos]=letra_usuario 
            pos+=1

      if letra_usuario not in palabra:    # SI la letra no esta dentro aumenta el contador
            cont+=1
      
      if adivinar == palabra:
            print("Has ganado!")
            break

      print(adivinar)


