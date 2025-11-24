# Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
# Ejemplo: original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
# invertido = {"Buenos Aires": "Argentina", "Santiago": "Chile"}

def invertir_diccionario(original):
    invertido = {}
    for pais, capital in original.items():
        invertido[capital] = pais
    return invertido

original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia", "Perú": "Lima", "Colombia": "Bogotá"}
invertido = invertir_diccionario(original)

print("Diccionario original:", original)
print("Diccionario invertido:", invertido)


