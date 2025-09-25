#Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

inicio= int(input(" Ingrese el numero desde donde quiere comenzar "))
final= int(input( " Ingrese hasta que numero desea sumar "))
suma= 0
for i in range(inicio + 1, final):
    suma = suma + i

print (" La suma de los numeros comprendidos entre ellos excluyendolos es: ", suma)
            