# Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. 
# Cada línea debe tener: nombre,precio,cantidad

with open('productos.txt', 'w') as file:
    file.write(" Arroz, 1.500, 20\n")
    file.write(" Yerba, 2.500, 17\n")
    file.write(" Yogurt, 1.100, 12\n")

with open('productos.txt', 'r') as file:
    contenido = file.read()
    print("Contenido del archivo productos.txt:")
    print(contenido)