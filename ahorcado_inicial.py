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
z = 0

while (cont <= 6):

      letra = str(input("Introduce una letra para adivinar: "))

      def get_palabra_secreta():
            palabras = ["casa","coche","tomate","lechuga"]
            x = random.choice(palabras)
            y = len(x)
            return x,y


      def print_horca(numero):
            print(AHORCADO[2])

      x,y = get_palabra_secreta()

      while (cont <= 6):
            print(AHORCADO[cont])
            cont = cont + 1

      if cont >= 6:
            print("Has muerto")
            exit
      
      print(x,y)

      while (z != y):
            adivinar.append("-")
            z = z + 1             
      
      print(adivinar)


