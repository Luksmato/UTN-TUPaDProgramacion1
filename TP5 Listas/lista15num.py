# Generar una lista con 15 números enteros al azar entre 1 y 100.
# Crear una lista con los pares y otra con los impares.
# Mostrar cuántos números tiene cada lista.

import random
numeros = []
for i in range(15):
    numeros.append(random.randint(1, 100))
print(" Lista de 15 numeros generados al azar :")
for numero in numeros:
    print(numero)

pares = []
impares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print ( " Lista de numeros pares :" )
for par in pares:
    print(par)
    
print ( " Lista de numeros impares :" )
for impar in impares:
    print(impar)

print("Cantidad de números pares:", len(pares))
print("Cantidad de números impares:", len(impares))

