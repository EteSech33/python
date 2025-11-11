"""
Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir como parámetro la cantidad sin IVA 
y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
"""

def impuesto(dinero,iva):
    cantidad = (dinero * (iva/100));
    return cantidad

cantidad = impuesto(2500,15)

print(cantidad)
