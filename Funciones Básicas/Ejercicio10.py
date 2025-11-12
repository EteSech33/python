"""
Ejercicio 10: Conversor distancias
Escribe un programa que pida una distancia en centímetros y que escriba esa distancia en kilómetros, metros y centímetros (escribiendo todas las unidades).

CONVERTIDOR DE CM A KM, M Y CM
Escriba una distancia en centímetros: 0
Escriba una distancia mayor que cero.
CONVERTIDOR DE CM A KM, M Y CM
Escriba una distancia en centímetros: 43210
43210 centímetros son 0 km 432 m 10 cm.
CONVERTIDOR DE CM A KM, M Y CM
Escriba una distancia en centímetros: 56
56 centímetros son 0 km 0 m 56 cm.
"""

cm = int(input("Escriba una distancia en centímetros: "))

def distancia(cm):

    m = int(cm/100)
    km = int(cm/100000)

    if (cm <= 0):
        print(f"Escriba una distancia mayor que {cm} centímetros.")
    else:
        cm = str(cm)[-2:]
        print(f"{cm} centímetros son {km} km {m} m {cm} cm.")

distancia(cm)

    
