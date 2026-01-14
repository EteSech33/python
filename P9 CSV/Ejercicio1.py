import csv
# Gabriel Kirilov Chonov

# Cargar el CSV de distancias

datos = []

with open("distanciasAndalucia.csv", "r", newline="") as distancias:
    reader = csv.DictReader(distancias)
    for linea in reader:
        datos.append(linea)

origen = str(input("Indique el punto de salida: "))
destino = str(input("Indique el destino: "))
combustible = str(input("¿Qué combustible usa tu coche?: "))
litros = float(input("¿Cuantos litros consume tu coche cada 100 km?: "))
precios_litro_combustible = { "diesel": 1.54, "gasolina95": 1.7,  "gasolina98": 1.75, "gas": 1.1}

km = 0

for linea in datos:
    if linea["origen"] == origen and linea["destino"] == destino:
        km = int(linea["km"])
        precio_litro = precios_litro_combustible[combustible]
        coste_total = (km/100)*litros*precio_litro
        print(f"Entre {origen} y {destino} hay {km}. El coste de tu viaje será de {coste_total:.2f}")
        break