# Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, 
# y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed()

def es_palindromo (palabra):
# Si la longitud de la palabra (caracteres) es 0 o 1, es un palindromo   
    if len(palabra) <= 1:
        return True
    else:
# Compara el primer y ultimo caracter de la palabra       
        if palabra[0] != palabra[-1]:
            return False
        else:
# Llama recursivamente a la función con la palabra sin el primer y ultimo caracter
            return es_palindromo(palabra[1:-1])
        
palabra = input( " Ingrese una palabra sin espacios ni tildes: ")
if es_palindromo(palabra):
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")

