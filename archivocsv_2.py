import csv

lista = []
# Leer el CSV utiliza DictReader - Convierte el csv a diccionarios
with open("peliculas.csv", "r", newline="") as peliculas:
    reader = csv.DictReader(peliculas)
    for row in reader:
        lista.append(row)
        print(row)

for pelicula in lista:
    print(f"Tenemos {pelicula['Titulo']}, Genero {pelicula['Genero']}, y Nota {pelicula['Nota']}")

# Escribir linea en el csv con DictWriter
fields=["Titulo","Genero","Fecha","Nota"]
new_film=['Titulo':'El Resplandor','Genero':'Terror','Fecha':'1998','Nota':'10']