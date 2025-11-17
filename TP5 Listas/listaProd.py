# Pedir al usuario que cargue 5 productos en una lista.
# Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []
print(" Ingrese 5 productos: ")

for i in range(5):
    producto = input(f"Producto {i+1}: ")
    productos.append(producto)      

productos_ordenados = sorted(productos)
print("Lista de productos ordenada alfabéticamente:")
for producto in productos_ordenados:
    print(producto)

producto_a_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar)
    print(f"Producto '{producto_a_eliminar}' eliminado.")   
else:
    print(f"Producto '{producto_a_eliminar}' no encontrado en la lista.")

print("Lista actualizada de productos:")
for producto in productos:
    print(producto) 
    