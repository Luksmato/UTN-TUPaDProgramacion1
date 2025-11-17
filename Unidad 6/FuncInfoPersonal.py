# Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: 
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal (nombre, apellido, edad, residencia):
    print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre_usuario = input("Ingrese su nombre: ")
apellido_usuario = input("Ingrese su apellido: ")  
edad_usuario = input("Ingrese su edad: ")
residencia_usuario = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)