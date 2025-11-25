# Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, 
# sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista.


lista_productos = [
    "Arroz, 1.500, 20",
    "Yerba, 2.500, 17",
    "Yogurt, 1.100, 12"
]

with open('productos.txt', 'w') as file:
    file.write(" Arroz, 1.500, 20")
    file.write(" Yerba, 2.500, 17")
    file.write(" Yogurt, 1.100, 12")

print("Archivo productos.txt sobrescrito con los productos actualizados.")
with open('productos.txt', 'r') as file:
    contenido = file.read()
    print("Contenido del archivo productos.txt:")
    print(contenido)    

