"""
Ejercicio 9
Escribe un programa que solicite un texto y que escriba el texto en mayúsculas, en minúsculas,  
con la primera letra en mayúscula, y con la primera letra de cada palabra en mayúscula.
"""
def texto():
    txt = input("Introduce un texto: ")
    txt_may = txt.upper()
    txt_min = txt.lower()
    txt_cap = txt.capitalize()
    txt_tit = txt.title()
    return txt, txt_may, txt_min, txt_cap, txt_tit

txt, txt_may, txt_min, txt_cap, txt_tit = texto()

print(txt)
print(txt_may)
print(txt_min)
print(txt_cap)
print(txt_tit)