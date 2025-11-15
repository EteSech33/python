"""
Crea una función llamada file_type que reciba el nombre de un archivo y nos indique el tipo de archivo en función de su extensión.  
Vamos a suponer que el nombre del archivo no va contener puntos.
Si el archivo es (.jpg, .jpeg, o .png) nos dirá que es una imagen.
Si el archivo es .pdf nos dirá que es un documento PDF.
Si el archivo es (.rar, .zip, o .tar.gz) nos dirá que es un comprimido.
En cualquier otro caso, la función imprimirá un mensaje indicando “Tipo de archivo no reconocido”.

Ejemplo de llamada a la función:
file_type(“apuntes.pdf”)

Resultado:
El archivo apuntes.pdf es un documento PDF.
"""

def file_type(file):
    # Listas de 
    imagenes = [".jpg",".jpeg",".png"]
    comprimidos = [".rar",".zip",".tar.gz"]

    punto = file.find(".")
    ext = file[punto:]
    
    if (ext == ".pdf"):
        print(f"Tu archivo {ext} es un documento pdf.")
        exit
    elif ext in imagenes: # Si la extension está dentro de imagenes imprime que es una imagen
        print(f"Tu archivo {ext} es una imagen.")
        exit

    elif ext in comprimidos: # Si la extension está dentro de comprimidos imprime que es un comprimido
        print(f"Tu archivo {ext} es un comprimido.")
        exit   
    else:
        print("Tipo de archivo no reconocido.")

file_type("foto.png")
