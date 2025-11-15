"""
Ejercicio 9: Notas - IF 
Crea una función que reciba una nota numérica con decimales. 
La función deberá devolver si la calificación es MATRÍCULA DE HONOR, SOBRESALIENTE, NOTABLE, BIEN, SUFICIENTE o INSUFICIENTE.
Deberás tener en cuenta si la nota tiene un valor incorrecto.
"""

def notas(nota):
    if (nota < 5):
        print(f"Has sacado un {nota}, es un INSUFICIENTE")
    elif (nota >= 5):
        print(f"Has sacado un {nota}, es un SUFICIENTE")
    elif (nota >= 6):
        print(f"Has sacado un {nota}, es un BIEN")
    elif (nota >= 7):
        print(f"Has sacado un {nota}, es un NOTABLE")
    elif (nota >= 8):
        print(f"Has sacado un {nota}, es un NOTABLE ALTO")
    elif (nota >= 9):
        print(f"Has sacado un {nota}, es un SOBRESALIENTE")
    elif (nota == 10):
        print(f"Has sacado un {nota}, es un MATRICULA DE HONOR")
    
notas(8.237)

