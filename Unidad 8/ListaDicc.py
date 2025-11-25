# Cargar productos en una lista de diccionarios: Al leer el archivo,
# cargar los datos en una lista llamada productos, donde cada elemento sea un diccionario con claves: nombre, precio, cantidad.

productos = []

with open('productos.txt', 'w') as file:
    file.write(" Arroz, 1.500, 20\n")
    file.write(" Yerba, 2.500, 17\n")
    file.write(" Yogurt, 1.100, 12\n")
    
with open('productos.txt', 'r') as file:
   for line in file:
        producto, precio, cantidad = line.strip().split(',')
        productos.append({'nombre': producto, 'precio': precio, 'cantidad': cantidad})

print(productos)
