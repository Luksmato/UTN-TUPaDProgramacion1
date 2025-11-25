# Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30


with open('productos.txt', 'w') as file:
    file.write(" Arroz, 1.500, 20\n")
    file.write(" Yerba, 2.500, 17\n")
    file.write(" Yogurt, 1.100, 12\n")

with open('productos.txt', 'r') as file:
    contenido = file.readlines()
    for linea in contenido:
        linea = linea.strip()
        partes = linea.split(",")
        nombre = partes[0].strip()
        precio = partes[1].strip()
        cantidad = partes[2].strip()
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

