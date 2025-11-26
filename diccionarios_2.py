fruteria = {"peras":1.5, "manzanas":2.6, "platanos":2.8}

fruta = input("Introduce la fruta que quieres: ")
peso = int(input("¿Cuantos kg quieres? "))

precio_kilo = fruteria[fruta]
precio_total = precio_kilo * peso
