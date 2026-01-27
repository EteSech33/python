"""
Ejercicio 12: Horas, minutos y segundos.
Escribir dos funciones que permitan calcular:

La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
Ejemplo: convertir_a_horas_minutos_segundos(segundos)
La función deberá devolver tres variables, las horas, los minutos y los segundos.

La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
Ejemplo: convertir_a_segundos(horas,minutos,segundos)
"""

def convertir_a_horas_minutos_segundos(s):
    m = s/60
    h = s/360
    return s,h,m

s,h,m = convertir_a_horas_minutos_segundos(127)
print(f"Tenemos {h:.3f} horas, {m:.2f} minutos y {s} segundos.") #Con ":.3f" cogemos los 3 primeros decimales, con 2 los 2 primeros.

def convertir_a_horas_minutos_segundos(h,m,s):
    m = s*60
    h = s*360
    x = s + m + h
    return x

x = convertir_a_horas_minutos_segundos(2,27,13)
print(f"Tenemos un total de {x} segundos.")
