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

def validar_texto(texto):
    return texto.strip() != ""


def buscar_codigo(codigo, productos):
    codigo = codigo.upper()

    for cod in productos:
        if cod.upper() == codigo:
            return True

    return False


def leer_texto_no_vacio(mensaje):
    while True:
        texto = input(mensaje).strip()

        if validar_texto(texto):
            return texto
        else:
            print("El dato no puede estar vacío.")


def stock_categoria(categoria, productos, inventario):
    total = 0

    for codigo in productos:
        datos = productos[codigo]

        if datos[1].lower() == categoria.lower():
            total = total + inventario[codigo][0]

    print("Stock disponible:", total)


def ejecutar_stock_categoria(productos, inventario):
    categoria = leer_texto_no_vacio("Ingrese categoría: ")
    stock_categoria(categoria, productos, inventario)

def leer_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Debe ingresar un número entero.")


def buscar_precio(precio_min, precio_max, productos, inventario):
    encontrados = []

    for codigo in productos:
        precio = productos[codigo][2]
        stock = inventario[codigo][0]

        if precio >= precio_min and precio <= precio_max and stock > 0:
            nombre = productos[codigo][0]
            encontrados.append(nombre + "--" + codigo)

    encontrados.sort()

    return encontrados


def ejecutar_buscar_precio(productos, inventario):

    while True:
        precio_min = leer_entero("Ingrese precio mínimo: ")

        if precio_min >= 0:
            break
        else:
            print("El precio mínimo debe ser mayor o igual a 0.")

    while True:
        precio_max = leer_entero("Ingrese precio máximo: ")

        if precio_max >= 0:
            break
        else:
            print("El precio máximo debe ser mayor o igual a 0.")

    if precio_min > precio_max:
        print("El precio mínimo no puede ser mayor que el precio máximo.")
        return

    productos_encontrados = buscar_precio(precio_min, precio_max, productos, inventario)

    if len(productos_encontrados) > 0:
        print("\nProductos encontrados:")
        print(productos_encontrados)
    else:
        print("No existen productos en ese rango de precio.")

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
            ejecutar_stock_categoria(productos, inventario)

        elif opcion == 2:
            ejecutar_buscar_precio(productos, inventario)

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
