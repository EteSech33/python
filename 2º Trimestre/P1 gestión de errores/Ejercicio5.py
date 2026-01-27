def leer_archivo(nombre):
    archivo = open(nombre, 'r')
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)
    archivo.close()

nombre_archivo = input("Introduce el nombre del archivo: ")
leer_archivo(nombre_archivo)
