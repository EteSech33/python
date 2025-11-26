# Diccionarios

# Los diccionarios usan llaves
paises = {"España":"Madrid", "Francia":"París", "Portugal":"Lisboa", "Alemania":"Berlín"}

print(paises)

# Imprime el valor correspndiente a la clave España
print(paises["España"])
print(paises.get("Portugal"))

#print(paises["Islandia"]) # Produce keyError porque la clave Islandia no está en el diccionario
print(paises.get("Islandia"))

print(paises.keys()) # Imprime las claves del diccionario
print(paises.values()) # Imprime los valores del diccionario

# Añadir un elemento al diccionario o modificar uno existente
paises["Islandia"] = "Rekiavik"
paises["Islandia"] = "Rekiavik"

print(paises)

# Recorrer el diccionario con un for
for clave in paises:
    print(f"El país {clave} tiene la capital en {paises[clave]}")

for clave,valor in paises.item():
    print(f"El pais {clave} tiene la captial en {valor}")