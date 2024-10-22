Postres = {} # Diccionario que almacena los postres
 
def imprimir(nombre_postre): # Imprimir la lista de todos sus ingredientes
    if nombre_postre in Postres:
        print(f"Ingredientes de {nombre_postre}: {', '.join(Postres[nombre_postre])}")
    else:
        print(f"El postre '{nombre_postre}' no se encuentra en la lista.\n")

def insertar(nombre_postre, nuevos_ingredientes): # Insertar nuevos ingredientes a su lista
    if nombre_postre in Postres:
        Postres[nombre_postre].extend(nuevos_ingredientes)
        print(f"Se han agregado los ingredientes {nuevos_ingredientes} al postre {nombre_postre}.\n")
    else:
        print(f"El postre '{nombre_postre}' no se encuentra en la lista.\n")

def eliminar(nombre_postre, ingrediente): # Eliminar alguno de sus ingredientes
    if nombre_postre in Postres:
        if ingrediente in Postres[nombre_postre]:
            Postres[nombre_postre].remove(ingrediente)
            print(f"El ingrediente '{ingrediente}' ha sido eliminado de {nombre_postre}.\n")
        else:
            print(f"El ingrediente '{ingrediente}' no se encuentra en la lista de {nombre_postre}.\n")
    else:
        print(f"El postre '{nombre_postre}' no se encuentra en la lista.\n")

def dar_de_alta_postre(nombre_postre, ingredientes): # Dar de alta un postre con sus ingredientes
    if nombre_postre not in Postres:
        Postres[nombre_postre] = ingredientes
        print(f"El postre '{nombre_postre}' ha sido dado de alta con los ingredientes: {ingredientes}.\n")
    else:
        print(f"El postre '{nombre_postre}' ya existe en la lista.\n")

def dar_de_baja_postre(nombre_postre): # Eliminar el postre
    if nombre_postre in Postres:
        del Postres[nombre_postre]
        print(f"El postre '{nombre_postre}' ha sido eliminado.\n")
    else:
        print(f"El postre '{nombre_postre}' no se encuentra en la lista.\n")

def mostrar_todos_los_postres():
    if Postres:
        print("Lista de postres y sus ingredientes:")
        for postre, ingredientes in Postres.items():
            print(f"{postre}: {', '.join(ingredientes)}")
        print()  # Salto de línea adicional
    else:
        print("No hay postres en la lista.\n")

def eliminar_ingredientes_repetidos():
    for postre, ingredientes in Postres.items(): # Convertir la lista de ingredientes a un conjunto
        ingredientes_unicos = list(set(ingredientes))
        Postres[postre] = ingredientes_unicos
    print("Se han eliminado los ingredientes repetidos de todos los postres.\n")

def menu():
    print(" ------------ ")
    print("Menú de Postres:")
    print(" ------------ ")
    print("1. Dar de alta un postre")
    print("2. Dar de baja un postre")
    print("3. Imprimir ingredientes del postre")
    print("4. Insertar ingredientes del postre")
    print("5. Eliminar ingrediente de un postre")
    print("6. Mostrar todos los postres con sus ingredientes")
    print("7. Eliminar todos los ingredientes repetidos")
    print("8. Salir")

def opciones():
    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre_postre = input("\nNombre del postre: ")
            ingredientes = input("Lista de ingredientes separados por comas: ").split(", ")
            dar_de_alta_postre(nombre_postre, ingredientes)

        elif opcion == "2":
            nombre_postre = input("Nombre del postre a eliminar: ")
            dar_de_baja_postre(nombre_postre)

        elif opcion == "3":
            nombre_postre = input("Nombre del postre para imprimir ingredientes: ")
            imprimir(nombre_postre)

        elif opcion == "4":
            nombre_postre = input("Nombre del postre para agregar ingredientes: ")
            nuevos_ingredientes = input("Nuevos ingredientes separados por comas: ").split(", ")
            insertar(nombre_postre, nuevos_ingredientes)

        elif opcion == "5":
            nombre_postre = input("Nombre del postre para eliminar ingrediente: ")
            ingrediente = input("Nombre del ingrediente a eliminar: ")
            eliminar(nombre_postre, ingrediente)

        elif opcion == "6":
            mostrar_todos_los_postres()
            
        elif opcion == "7":
            eliminar_ingredientes_repetidos()
            
        elif opcion == "8":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.\n")

opciones() # Ejecución del programa principal
