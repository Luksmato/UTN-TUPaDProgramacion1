# Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

segundos_usuario = int(input(" Por favor, ingresa una cantidad de segundos: "))
horas_convertidas = segundos_a_horas (segundos_usuario)

print(f"La cantidad de horas correspondientes a {segundos_usuario} segundos es: {horas_convertidas} horas.")