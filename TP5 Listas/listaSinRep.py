# Dada una lista con valores repetidos:
# datos = [ 1, 3, 5, 3, 7, 1, 9, 5, 3 ]
# Crear una nueva lista sin elementos repetidos.
# Mostrar el resultado.

datos = [ 1, 3, 5, 3, 7, 1, 9, 5, 3 ]
datos_sin_repetidos = []

i = 0
while i < len(datos):
    if datos[i] not in datos_sin_repetidos:
        datos_sin_repetidos.append(datos[i])
    i += 1

print("Lista sin elementos repetidos:", datos_sin_repetidos)