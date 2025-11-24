# Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

def cargar_contactos():
    contactos = {}
    for i in range(5):
        nombre = input('Ingrese el nombre del contacto: ')
        numero = input('Ingrese su numero telefonico: ')
        contactos[nombre] = numero
    return contactos

def consulta_contacto(contactos):
    nombre = input('Ingrese el nombre del contacto a consultar: ')
    if nombre in contactos:
        print(f'El numero de {nombre} es {contactos[nombre]}')
    else:
        print('El contacto no esta agendado')

contactos = cargar_contactos()

consulta_contacto(contactos)