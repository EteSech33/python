"""
Crea una función que detecte si dos palabras son anagramas. Si son anagramas devolverá True, sino False.
Para saber si dos palabras son anagramas se han de seguir los siguientes pasos:
Convertir ambas palabras en minúsculas.
Después, convertir las palabras de string a listas con la función list.
Una vez que ambas cadenas son listas, las ordenamos.
Convertimos de nuevo las listas en cadenas **. En este punto ambas cadenas ya están ordenadas alfabéticamente y en minúsculas.
Si ambas cadenas son iguales, decimos que una palabra es anagrama de la otra.
** Puedes convertir una lista en cadena de la siguiente forma:
A = ["a", "b", "c"]
StrA = "".join(A)
print(StrA)
"""
p1 = "poder"
p2 = "Pedro"

def anagrama(p1,p2):
    p1 = p1.lower()
    lista_p1=list(p1)
    lista_p1.sort()
    
    p2 = p2.lower()
    lista_p2=list(p2)
    lista_p2.sort()
    if lista_p1 == lista_p2:
        print(f"Tus palabras {p1} y {p2} son anagramas.")
    else:
        print(f"Tus palabras {p1} y {p2} NO son anagramas.")

anagrama(p1,p2)
    