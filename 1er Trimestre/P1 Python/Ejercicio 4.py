"""
Ejercicio 4
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, 
y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
"""
def persona():
    peso = float(input("Indicame tu peso en kg, solo el número: "))
    estatura = float(input("Indicame tu estatura en metros, solo el número: "))
    return peso/estatura

imc = persona()

print(f"Tu indice de masa corporal es {imc:.2f}")