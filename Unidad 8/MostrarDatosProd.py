# Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. Recorrer la lista de productos y, 
# si lo encuentra, mostrar todos sus datos. Si no existe, mostrar un mensaje de error.


with open('productos.txt', 'w') as file:
    file.write(" Arroz, 1.500, 20\n")
    file.write(" Yerba, 2.500, 17\n")
    file.write(" Yogurt, 1.100, 12\n")

with open('productos.txt', 'r') as file:
    contenido = file.read()
    print("Contenido del archivo productos.txt:")
    print(contenido)
    
nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
encontrado = False
with open('productos.txt', 'r') as file:
    for linea in file:
        partes = linea.strip().split(",")
        nombre = partes[0].strip()
        precio = partes[1].strip()
        cantidad = partes[2].strip()
        if nombre == nombre_buscar:
            print(f"Producto encontrado: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
            encontrado = True
            break
if not encontrado:
    print("Producto no encontrado.")

