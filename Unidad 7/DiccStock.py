# Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

productos = {"arroz": 12, "fideos": 15, "aceite": 5, "sal": 8, "yerba": 20}

def consultar_stock(productos):
    producto= input("Ingrese el nombre del producto a consultar:")
    if producto in productos:
        print(f"El stock de {producto} es: {productos[producto]}")
    else:
        print("El producto no existe en el stock.")

def agregar_unidades(productos):
    producto = input("Ingrese el nombre del producto al que desea agregar unidades:")
    if producto in productos:
        unidades = int(input("Ingrese la cantidad de unidades a agregar:"))
        productos[producto] += unidades
        print(f"Se han agregado {unidades} unidades a {producto}")
    else:
        print("El producto no existe en el stock.")

def agregar_nuevo_producto(productos):
    producto = input("Ingrese el nombre del nuevo producto:")
    if producto not in productos:
        unidades = int(input("Ingrese la cantidad de unidades del nuevo producto:"))
        productos[producto] = unidades
        print(f"Se ha agregado el producto {producto} con {unidades} unidades.")
    else:
        print("El producto ya existe en el stock.")

while True:
    print("\nOpciones:")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades a un producto existente")
    print("3. Agregar un nuevo producto")
    
    opcion = input("Seleccione una opción (1, 2, 3): ")
    
    if opcion == "1":
        consultar_stock(productos)
    elif opcion == "2":
        agregar_unidades(productos)
    elif opcion == "3":
        agregar_nuevo_producto(productos)
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")


