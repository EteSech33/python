def leer_archivo(nombre):
    archivo = ""
    try:
        archivo = open(nombre, 'r')
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
    except FileNotFoundError:
        print(f"No se ha podido encontrar el archivo {nombre}")
    finally:
        if archivo != "":
            archivo.close()

nombre = input("Introduce el nombre del archivo: ")
leer_archivo(nombre)

