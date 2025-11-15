"""
Crear un programa que pida al usuario su correo electrónico.
Ejemplo: msanchez@ciudadjardin.org. 
El programa deberá mostrar por pantalla el nombre de usuario, es decir todo el texto hasta la @ 
y el dominio, es decir, desde la @ hasta el final de la cadena. 
"""
var = input(str("Introduce tu correo electrónico: "))

buscar = var.find("@")

var = var[buscar:]

print(f"Tu dominio es: {var}")
