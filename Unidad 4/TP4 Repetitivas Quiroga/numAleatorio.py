# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

from random import *
numero= int(input( " Adivine el numero entre 0 y 9 : "))
intento = 1
while numero != (randint(0,9)):
    numero= int(input( " Adivine el numero entre 0 y 9 : "))
    intento = intento + 1

print (" Adivinaste el numero en ", intento, " intentos ")