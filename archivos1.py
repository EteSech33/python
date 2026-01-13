# Manejo de archivos

# Escribir datos en un archivo

# Abre el fichero en modo sobreescritura
# El cursor se posiciona al principio
f = open("planetas.txt", "w")
f.write("Mercurio\n")
f.write("Venus\n")
f.close()

# Abrimos el mismo archivo en modo append (a)
f = open("planetas.txt","a")
f.write("Tierra\n")
f.close()

# Abrimos el archivo en modo lectura (r)
f = open("planetas.txt","r")
planetas = f.read()
f.close()
print(planetas)

# Añadimos control de errores
try:
    f = open("planetas.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("El fichero no existe.")
else: # Si no se produjo error, cerramos el fichero
    f.close()

# Añadir with - El fichero se cierra automáticamente
with open("planetas.txt", "r") as f:
    for line in f:
        print(f"Planeta: {line}")

# Version 2
with open("planetas.txt", "r") as f:
    lineas = f.readlines()
    for linea in lineas:
        print(linea)