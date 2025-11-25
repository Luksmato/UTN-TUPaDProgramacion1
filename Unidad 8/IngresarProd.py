# Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos,
# le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) y lo agregue al archivo sin borrar el contenido existente.

with open('productos.txt', 'r') as file:
    contenido = file.read()
    print("Contenido del archivo productos.txt:")
    print(contenido)

nuevo_producto = input( " Ingrese un nuevo producto (nombre, precio, cantidad):" )
with open('productos.txt', 'a') as file:
    file.write("\n" + nuevo_producto )

with open('productos.txt', 'r') as file:
    contenido = file.read()
    print("Contenido actualizado del archivo productos.txt:")
    print(contenido)


