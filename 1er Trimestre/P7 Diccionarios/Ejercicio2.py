divisas = {"Euro":"€", "Dolar":"$", "Libra":"£", "Yen": "¥"}

var = str(input("Introduce la divisa que quieres obtener: ")).lower().capitalize()


if var in divisas:
    print(f"Tenemos 200{divisas[var]}")
else:
    print(f"Nos hemos quedado sin {var}")