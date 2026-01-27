print("Bienvenido a la tómbola: ")

# Array de Nº de premios
papeletas = ['premio2','premio4','premio1','premio3','premio4', 'premio5', 'premio5']
# Diccionario de tipos premios
tombola = { 'premio1':'perrito piloto', 'premio2':'batidora', 'premio3':'coche teledirigido','premio4': 'chocolatina' }

try:
    numero=int(input("Introduce un número: "))
    premio=papeletas[numero]
    print(f"Enhorabuena, has sido premiado con el premio {premio} que corresponde a: {tombola[premio]}")
except ValueError:
    print("No has introducido un número.")
except KeyboardInterrupt:
    print("\nEl usuario se ha salido del programa.")
except IndexError:
    print(f"El número {numero} ha roto la tombola! Prueba de nuevo.")
except KeyError:
    print("No has coseguido premio.")

"""
Dado el siguiente bloque de código. 
Gestiona detalladamente todos los errores que pueden producirse, 
mostrando un mensaje de error adecuado en cada caso. 
Si no se consigue premio, se indicará “Suerte para la próxima”
"""