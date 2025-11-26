def validar():
    especial = ["!","@","#","$","%","^","&","*"]
    contr = str(input("Introduce tu contraseña para que sea validada: "))
    contr_lista = list(contr)

    a = False
    b = False
    c = False
    d = False

    if len(contr) >= 8: # VErifica que sea mayor de 8 caracter
        for letras in contr_lista:
            if letras.isupper():
                a = True
                exit
            # Comprueba si una caracter de la contraseña es mayúscula, devuelve False    
            if letras.islower():
                b = True
                exit
            # Comprueba si una caracter de la contraseña es minúscula, devuelve False 
            if letras.isnumeric():
                c = True
                exit
            # Comprueba si una caracter de la contraseña es numerico, devuelve False 
            if letras in especial:
                d = True
            # Comprueba que hay un caracter especial en la contraseña, sino devuelve False
    else:
        x = False
    # Si la contraseña es menor de 8 devuelve false

    # Comprueba si las variables son False o True, si todas las condiciones anteriores
    # se han cumplido, devuelve True. Si la contraseña no las cumple, devuelve False
    if a==True and b==True and c==True and d==True:
        x = True
    else:
        x = False
    return x

resultado = validar()

print(resultado)