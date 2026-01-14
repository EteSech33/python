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
new_film={'Titulo':'El Resplandor','Genero':'Terror','Fecha':'1998','Nota':'10'}
with open("peliculas.csv","a",newline="") as peliculas:
    writer = csv.DictWriter(peliculas,fields)
    writer.writerow(new_film)


# Escribir un csv nuevo
fields2 = ["Marca","Modelo","Precio"]
coche1 = {'Marca':'Tesla','Modelo':'S','Precio':'5'}
coche2 = {'Marca':'BMW','Modelo':'M3','Precio':'104000'}
coche3 = {'Marca':'Polloneta','Modelo':'Pollo','Precio':'29323'}
coches = [coche1, coche2, coche3]

with open("concesionario.csv", "w", newline="") as concesionario:
    writer = csv.DictWriter(concesionario,fields2)
    writer.writeheader()
    writer.writerows(coches)