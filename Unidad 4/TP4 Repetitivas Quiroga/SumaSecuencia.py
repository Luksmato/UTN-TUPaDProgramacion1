# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0

numero= int(input( " Ingrese un numero entero "))
suma= numero
while not numero == 0:
    numero=  int(input (" Ingrese otro entero a sumar y 0 en caso de querer finalizar "))
    suma= suma + numero

print (" La suma de todos esos numeros es: ", suma)