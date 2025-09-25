# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. 
suma = 0
for i in range(100):
    numero = int(input(" Ingrese un numero entero: "))
    suma = suma + numero

print( " La media de los numeros que ingreso es: ", suma / 100)
