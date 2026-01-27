"""
Ejercicio 7
Escribe un programa que solicite al usuario una temperatura en escala Fahrenheit (debe permitir decimales) 
y le muestre el equivalente en grados Celsius. 
La fórmula de conversión que se usa para este cálculo es: Celsius = (5/9) * (Fahrenheit-32). 
Mostrar el resultado utilizando dos decimales.
"""
def solicitar():
    F = float(input("Introduce los grados en Farenheit: "))
    return ((F - 32) * (5/9))

print (f"{solicitar()}º Celcius")