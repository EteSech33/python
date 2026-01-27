archivo = input("Introduce el nombre del archivo a abrir: ")
with open(archivo, 'r') as file:
    contenido = file.read()

print("Contenido del archivo:")
print(contenido)
