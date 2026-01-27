
datos = {"nombre":"","agnos":"","calle":"","ciudad":"","telefono":""}

# Pedimos al usuario el valor de cada clave, y lo metemos en el diccionario. 
# Ej: nombre:gabriel
datos["nombre"] = str(input("Introduce tu nombre: "))
datos["agnos"] = int(input("Introduce tu edad: "))
datos["calle"] = str(input("Introduce tu dirección: "))
datos["ciudad"] = str(input("Introduce tu ciudad: "))
datos["telefono"] = int(input("Introduce tu número de teléfono: "))

# Pintamos la frase con los datos
print(f"{datos['nombre']} tiene {datos['agnos']} años y vive en {datos['calle']},{datos['ciudad']} y su teléfono es {datos['telefono']}")