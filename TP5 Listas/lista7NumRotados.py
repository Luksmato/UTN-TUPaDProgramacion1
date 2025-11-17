# Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

numeros = [1, 2, 3, 4, 5, 6, 7]
rotados = []   

for i in range(len(numeros)):
    if i == 0:
        rotados.append(numeros[-1])  
    else:
        rotados.append(numeros[i - 1])    

print("Lista original de números: ")
for numero in numeros:
    print(numero)
print("Lista de números rotados a la derecha:" )
for numero in rotados:
    print(numero)

