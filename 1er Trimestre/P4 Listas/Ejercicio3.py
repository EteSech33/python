"""
Realiza una función para calcular el salario de un trabajador. 
La función deberá recibir el puesto del trabajador y el número de años de antigüedad en la empresa. 
A partir de estos dos parámetros, deberá calcular el sueldo del empleado, teniendo en cuenta el salario base, 
que cada año de antigüedad el sueldo sube según indica la siguiente tabla y por cada tres años completos el trabajador cobra un trienio. 
La función deberá devolver el sueldo total del empleado.
"""

puesto = ["Rrhh","Informática","Ventas"]
salario_base = [1200, 1500, 1000]
subida_anual = [12, 22, 10]
subida_trienio = [100, 120, 75]

puesto_usu = str(input("Introduce el puesto de trabajo al que perteneces: ").lower().capitalize())
antiguedad = int(input("Introduce los años de antiguedad trabajando: "))

if antiguedad == 0:
    print("Debes de introducir la cantidad de tiempo en años.\nEj: 3 meses es igual a 0.25 años")
    exit()
elif antiguedad < 0:
    print("No puedes trabajar años negativos.")
    exit()

def salario(puesto_usu,antiguedad):
    if puesto_usu in puesto: # Comprueba que el puesto de trabajo introducido, esta dentro de la lista de trabajos
        p = puesto.index(puesto_usu) # Busca la posicion del puesto introducido, si está, pone dentro "p" la posicion de ese puesto de trabajo.
    else:
        print("El puesto introducido no existe.")
    
    # Pone la posicion del puesto de trabajo en las demas listas.
    salario = salario_base[p] 
    anual = subida_anual[p]
    trienio = subida_trienio[p]

    x = anual * antiguedad
    y = trienio * (antiguedad // 3)
    salario = salario + x + y
    print(f"Tu salario es de {salario}€")

salario(puesto_usu,antiguedad)