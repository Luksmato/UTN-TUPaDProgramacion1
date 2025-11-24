# Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.


def palabras_unicas(frase):
    return set(frase.split())

def conteo_palabras(frase):
    contador_palabras = {}
    palabras = frase.split()
    for palabra in palabras:
        contador_palabras[palabra] = palabras.count(palabra)
    return contador_palabras

frase = input('Por favor, ingrese una frase: ')
print(f" Las palabras sin repeticiones de la frase son: {palabras_unicas(frase)}")
# print(palabras_unicas(frase))
print(f" La cantidad de veces que aparece cada palabra es: {conteo_palabras(frase)}")