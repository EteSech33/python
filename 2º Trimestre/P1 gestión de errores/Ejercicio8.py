print("Bienvenido a la tómbola: ")
papeletas = ['premio2','premio4','premio1','premio3','premio4', 'premio5', 'premio5']
tombola = { 'premio1':'perrito piloto', 'premio2':'batidora', 'premio3':'coche teledirigido','premio4': 'chocolatina' }
numero=int(input("Introduce un número: "))
premio=papeletas[numero]
print(f"Enhorabuena, has sido premiado con el premio {premio} que corresponde a: {tombola[premio]}")
