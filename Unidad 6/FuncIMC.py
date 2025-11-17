# Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). 
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc (peso, altura):
    imc = peso / altura ** 2
    return round (imc, 2)

peso_usuario = float (input (" Por favor, ingresa tu peso en kilogramos: " ))
altura_usuario = float (input (" Por favor, ingresa tu altura en metros: " ))
imc_usuario = calcular_imc (peso_usuario, altura_usuario)

print (f" Tu indice de masa corporal (IMC) es : {imc_usuario}" )

