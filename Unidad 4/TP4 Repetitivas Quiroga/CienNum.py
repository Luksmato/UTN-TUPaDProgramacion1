# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos.
numImpar = 0
numPar = 0
numPos = 0
numNeg = 0
for i in range(10):
    numero = int(input( " Ingrese un numero entero: "))
    if numero > 0:
        numPos= numPos + 1
        if numero % 2 == 0:
            numPar = numPar + 1
        else:
            numImpar = numImpar + 1
    elif numero < 0:
        numNeg= numNeg + 1
        if numero % 2 == 0:
            numPar = numPar + 1
        else:
            numImpar = numImpar + 1
    else:
        print( " No ha ingresado un numero entero valido " )
print(" La cantidad de numeros positivos es: ", numPos)
print(" La cantidad de numeros negativos es: ", numNeg)
print(" La cantidad de numeros pares es: ", numPar)
print(" La cantidad de numeros impares es: ", numImpar)
