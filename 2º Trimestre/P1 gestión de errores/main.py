import conversor

while True:

    print("--- Conversor ---")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Kilómetros a millas")
    print("4. Millas a kilómetros")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        c = float(input("Introduce los grados Celsius: "))
        fahrenheit = conversor.celsius_a_fahrenheit(c)
        print(f"{c:.2f}º grados celsius son {fahrenheit:.2f} grados Fahrenheit")

    elif opcion == "2":
        f = float(input("Introduce los grados Fahrenheit: "))
        celsius = conversor.fahrenheit_a_celsius(f)
        print(f"{f:.2f} Fahrenheit son {celsius:.2f}º grados Celsius")

    elif opcion == "3":
        km = float(input("Introduce los kilómetros: "))
        millas = conversor.kilometros_a_millas(km)
        print(f"{km:.2f} km equivalen a {millas:.2f} millas.")

    elif opcion == "4":
        millas = float(input("Introduce las millas: "))
        km = conversor.millas_a_kilometros(millas)
        print(f"{millas:.2f} millas equivalen a {km:.2f} km.")

    elif opcion == "5":
        print("Adiós!")
        break

    else:
        print("Opción no válida.")
