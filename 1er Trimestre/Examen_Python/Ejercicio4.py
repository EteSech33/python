opc = 0
lista = []

def agregar_tarea(lista,tarea):
    if tarea not in lista:
        lista.append(tarea)
        print("Tarea agregada.")
    else:
        print(f"La tarea {tarea} ya está en la lista.")

def eliminar_tarea(lista,tarea):
    if tarea in lista:
        lista.remove(tarea)
        print("Tarea eliminada.")
    else:
        print(f"La tarea {tarea} no está en la lista.")

def mostrar_tarea(lista):
    print("---- Tareas Pendietes ----")
    for tareas in lista:
        print(f"- {tareas}")


while opc != 4:
    print ("""
        --- MENÚ TODO LIST ---
        1.Agregar Tarea
        2.Eliminar Tarea
        3.Mostrar Tarea
        4.Salir
          """)
    opc = int(input("Introduce una opción: "))

    if opc == 1:
        tarea = str(input("Escribe la tarea a Agregar: "))
        agregar_tarea(lista,tarea)
    elif opc == 2:
        tarea = str(input("Escribe la tarea a Eliminar: "))
        eliminar_tarea(lista,tarea)

    elif opc == 3:
        mostrar_tarea(lista)

    elif opc == 4:
        print("Has salido del menú.")

    else: 
        print("Error")
