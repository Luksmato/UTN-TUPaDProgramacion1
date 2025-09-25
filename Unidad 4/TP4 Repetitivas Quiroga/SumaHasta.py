# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numero = int(input( " Introduce hasta que numero queres que sume: " ))
suma = 0
for i in range(0,numero + 1):
    suma = suma + i
print( " La suma de todos los numeros entre 0 y ",numero," es: ", suma)