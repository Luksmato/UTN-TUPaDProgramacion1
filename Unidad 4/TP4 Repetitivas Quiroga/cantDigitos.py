#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

numero= int(input(" Ingrese un numero entero ") )
cantDigitos= len(str(numero))
print (" La cantidad de digitos de su numero es: ", cantDigitos)