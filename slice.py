codigo="10520-2025"

# Slice de la cadena

print (codigo[0:4])
print (codigo[9])
print (codigo[-1]) # Último carácter de la cadena
print (codigo[-2]) # Penúltimo, asi sucesivamente
print (codigo[0:]) # Hasta el final
print (codigo[:])  # Hasta el final
print (codigo[:6]) # Del principio al final

telefono="+34557852545"

prefijo = telefono[0:3]

print(prefijo)

fecha ='25/09/2025'
dia=fecha[:2]
mes=fecha[3:5]
agno=fecha[6:10]

print(dia,mes,agno)

mensaje="saludo"
print(mensaje[::2]) #Desde el inicio hasta el final con salto 2
print(mensaje[::1]) #Desde el inicio hasta el final con salto 1
print(mensaje[::-1]) #Da la vuelta a la cadena de texto

posicion=mensaje.find("a") #Me devuelve la posicion de la primera letra a
print(posicion)

fecha2="5/9/2025"
dia=fecha2[:fecha2.find("/")]
mes_agno=fecha2[fecha2.find("/")+1:]
mes=mes_agno[:mes_agno.find("/")]
agno=mes_agno[mes_agno.find("/")+1:]
print(dia,mes,agno)

mes_agno.find("/",0,5)
print(fecha2.rfind("/")) #Busca el último carácter 