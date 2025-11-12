# Recorrer una lista
modulos = ["ASO", "SAD", "SRI", "OPT", "IAW"]

for modulo in modulos:
    print(f"Voy a  aprobar {modulo}")

paises = ["Japón", "Italia", "Francia"]

for pais in paises:
    print(f"He visitado {pais}")

tienda = ["pcs", "ratones", "teclados", "gráficas"]

for producto in tienda:
    print(f"Tengo {producto}")

dinero = [4, 5, 6, 1000]
total = 0
for importe in dinero:
    total+=importe

print(f"Tengo {total} euritos")


notas_aso = [5, 3, 9, 8]
# Media nota de aso
total_notas = len(notas_aso)
suma_notas = 0
for nota in notas_aso:
    suma_notas+=nota

media = suma_notas / total_notas
print(f"He sacado una media de {media}")


print (max(notas_aso)) # Me devuelve la nota más alta
print (min(notas_aso))

# Funcion RANGE

# range(start,stop,step)
# start donde empieza (incluido)
# stop donde finaliza (no incluido)
# step - salto NO es obligatorio

coches = ["Tesla", "BMW", "Toyota", "MG"]

print(range(0,5))

for num in range(0,5):
    print(num)

for num in range(3):
    print(num)

for num in range(4,10,2):
    print(num)

for num in range(0,6,-1):
    print(num)

for num in range(3):
    print(coches[num])