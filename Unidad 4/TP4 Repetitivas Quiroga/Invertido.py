# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario.

numero = int(input( " Ingrese un numero entero positivo: "))
numInv= 0
digito = 0
if numero > 0:
    while numero > 0:
        digito = numero % 10
        numInv = numInv * 10 + digito
        numero = numero // 10
    print( " El numero invertido es: ", numInv)
else:
    print( " No ha ingresado un numero valido ")
