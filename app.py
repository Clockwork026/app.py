def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Stock por categoría")
    print("2. Buscar productos por rango de precio")
    print("3. Actualizar precio")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Mostrar productos")
    print("7. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))

            if opcion >= 1 and opcion <= 7:
                return opcion
            else:
                print("Debe seleccionar una opción válida")

        except ValueError:
            print("Debe seleccionar una opción válida")

def ejecutar_programa():

    productos = {
        "P101":["Cuaderno","Papelería",2490,True],
        "P102":["Lápiz","Papelería",590,True],
        "P103":["Botella","Accesorios",6990,False],
        "P104":["Mochila","Accesorios",24990,True]
    }

    inventario = {
        "P101":[30,15],
        "P102":[120,50],
        "P103":[0,10],
        "P104":[8,25]
    }

    while True:

        mostrar_menu()

        opcion = leer_opcion()

        if opcion == 1:
            pass

        elif opcion == 2:
            pass

        elif opcion == 3:
            pass

        elif opcion == 4:
            pass

        elif opcion == 5:
            pass

        elif opcion == 6:
            pass

        elif opcion == 7:
            print("Programa finalizado.")
            break


ejecutar_programa()

#hola