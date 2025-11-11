alumnos = ["Ana","Paco","Rosario","Tamara","Benito"]

#Matricular un alumno
alumno= input("Introduzca el nombre del nuevo alumno: ")

#Verificar si el alumno esta en la lista, y si no está, añadirlo.
if alumno in alumnos:
    print(f"El alumno {alumno} ya esta matriculado.")
else:
    alumnos.append(alumno)
    print(f"El alumno {alumno} ha sido matriculado.")

print(alumnos)

# Recorrer la lista, para cada alumno.
for nombre in alumnos:
    print(f"{nombre} esta matrículado en 2ASIR.")

# Desmatricular un alumno
alumno = input("Introduce el nombre del alumno para desmatricular: ")
if alumno in alumnos:
    alumnos.remove(alumno)
    print(f"{alumno} ha sido desmatriculado.")
else:
    print("El alumno no esta matriculado.")

print(alumnos)
print(f"En nuestra escula hay {len(alumnos)} matriculados.")

# Ordenar de forma alfabetica
alumnos.sort()
print(alumnos)

# Ordenadar de forma alfabetica
alumnos.sort(reverse = True)
print(alumnos)