"""
El instituto dispone de la siguiente lista de alumnos:
alumnos_matriculados = [“Juan Sanchez”, “Luis Ramos”, “Ana Romero”, “Marta Moreno”]
Realizar un programa que muestre un menú:
1.Consultar matrícula.
2.Matricular a un alumno.
3.Anular la matrícula.
4.Obtener el total de alumnos.

La opción 1 pedirá el nombre de un alumno y nos dirá si está matriculado en nuestro instituto. 
La opción 2 pedirá un alumno y si no está matriculado, lo añadirá a la lista. 
La tercera opción pedirá un alumno y lo eliminará de la lista. La opción número 4 nos dirá el número de alumnos matriculados en nuestro instituto
"""

alumnos_matriculados = ["Juan Sanchez", "Luis Ramos", "Ana Romero", "Marta Moreno"]

print("1.Consultar matrícula.")
print("2.Matricular a un alumno.")
print("3.Anular la matrícula.")
print("4.Obtener el total de alumnos.")

var = str(input("Introduce el número de la opción deseada: "))

if var == "1":
    var_1 = str(input("Introduce el nombre del alumno: "))
    if var_1 in alumnos_matriculados:
        print(f"El alumno {var_1} está matriculado.")
    else:
        print(f"El alumno {var_1} no está matriculado.")

elif var == "2":
    var_2 = str(input("Introduce el nombre del alumno: "))
    if var_2 in alumnos_matriculados:
        print(f"El alumno {var_2} ya está matriculado.")
    else:
        alumnos_matriculados.append(var_2)
        print(alumnos_matriculados)

elif var == "3":
    var_3 = str(input("Introduce el nombre del alumno: "))
    if var_3 in alumnos_matriculados:
        alumnos_matriculados.remove(var_3)
        print(f"El alumno {var_3} ha sido desmatriculado.")
    else:
        print(f"El alumno {var_3} no está matriculado.")

elif var == "4":
    x = len(alumnos_matriculados)
    print(f"Hay un total de {x} alumnos matriculados.")
else:
    print("No has introducido una opción válida.")
