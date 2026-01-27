"""
Validar si un DNI es válido. 
Utilizaremos una lista que deberá contener las letras que muestra la imagen de abajo, 
teniendo en cuenta que la letra T estará en la posición 0 de la lista, la letra R en la posición 1 
y asi sucesivamente.
El algoritmo es el siguiente:
Pedir al usuario su DNI
La cadena de texto debe tener una longitud de 9 caracteres
Deberás recortar los caracteres del 1 al 8 (eliminando la letra). Puedes utilizar slice.
Comprueba si son números. Para ello puedes usar:
“1234”.isnumeric()  → Devolverá True si es un número.
Si es número, convierte esta cadena a un entero.
Divide este número entre 23 y obtén el resto. El resto de la división (operación normalmente conocida como módulo) indicará la letra que debe ocupar la posición 9 del string según la imagen siguiente:
Como punto extra, los siguientes DNI no son válidos independientemente que cumplan la validación explicada en los puntos anteriores: 00000000T, 00000001R y 99999999R.
"""
dni = str(input("Introduce tu DNI: "))
lista_numero = []
dni_revisado = []
letra = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
resto = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
mal = ["00000000T","00000001R","99999999R"]

def validar(dni):
    if len(dni) != 9: # Si la longitud del dni no es de 9 digitos, acaba el programa.
        print("Debes introducir 9 dígitos.")
        exit()
    x = dni[1:].upper()
    lista = list(x) # Listando los carácteres del DNI
    for caracter in lista:

        if caracter.isnumeric() == True: # Comprueba que los caracteres del DNI son numeros
            y = int(caracter)
            z = (y % 23)
            lista_numero.append(z)
        else:
            dni_revisado.append(caracter)

    for num in lista_numero: # Por cada numero en la lista numero, inserta esa posicion dentro de la lista "dni_revisado"
        letras = letra[num]
        dni_revisado.insert(0,letras)
    dni_valido = "".join(dni_revisado)

    if dni in mal:
        print("Tu DNI NO es válido.")
    else:
        print(f"Tu DNI {dni} es válido.")

validar(dni)