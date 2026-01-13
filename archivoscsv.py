import csv

# Primera forma de leer csv
with open("peliculas.csv", "r") as peliculas:
    reader = csv.reader(peliculas)
    for line in peliculas:
        print(line)
    
# Añadir linea al CSV
pelicula = ["Void","Contexto","2025","0"]

with open("peliculas.csv", "a", newline="") as peliculas:
    writer = csv.writer(peliculas)
    writer.writerow(pelicula)