while True:
    try:
        archivo = input("Introduce el nombre del archivo a abrir: ")
        with open(archivo, 'r') as file:
            contenido = file.read()
    except FileNotFoundError:
        print(f"No se ha podido encontrar el archivo {archivo}")
        break
    else:
        print("Contenido del archivo:")
        print(contenido)
        break
