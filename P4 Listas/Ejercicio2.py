"""
Realiza una función que reciba como parámetro un mes y devuelva el número de días que tiene ese mes.  
Debes resolver este ejercicio con listas. 
Pista: puedes crear una lista con los meses que tienen 30 días y otra con los meses que tienen 31.  
Puedes suponer que febrero tendrá 28 para simplificar.
Ejemplo:
dias_enero = calcular_dias(“enero”)
print(f”Enero tiene {dias_enero} días”)
Resultado: Enero tiene 31 días
"""

treinta = ["Abril","Junio","Septiembre","Noviembre"]
treinta_uno = ["Enero","Marzo","Mayo","Julio","Agosto","Octubre","Diciembre"]

mes = str(input("Introduce el mes del año: ").lower().capitalize())

def averiguar(mes):
    if mes in treinta:
        return 30
    elif mes in treinta_uno:
        return 31
    elif mes == "Febrero":
        return 28
    else:
        print("No has introducido un mes.")
        exit()

dias_enero = averiguar("enero")
print(f"{mes} tiene {dias_enero} días")