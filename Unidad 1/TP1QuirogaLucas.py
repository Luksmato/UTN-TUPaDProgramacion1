# Ejercicio 1
print ("Hola Mundo")

#Ejercicio 2
nombre = input (" Hola, dime tu nombre ")
print (f" Mucho gusto {nombre} !")

#Ejercicio 3

nombre = input ( " Hola, dime tu nombre ")
apellido = input ( " y tu apellido? ")
edad = input ( " que edad tienes? ")
lugar = input ( " y cual es tu lugar de residencia? ")
print (f"Hola, soy {nombre} {apellido}, tengo {edad} años de edad y resido en {lugar}")

#Ejercicio 4

import math
radio = input(" Cual es el radio del circulo ? ")
radio = float(radio)
area = math.pi * (radio**2)
perimetro = 2*math.pi*radio
print (f" el area del circulo es {area} y el perimetro es {perimetro} ")

#Ejercicio 5

segundos = int(input( " Ingrese los segundos que desea calcular "))
horas = segundos / 3600
horas = float(horas)
print ( "Esos segundos equivalen a ", horas , "horas")

#Ejercicio 6

numero = int (input(" Ingrese un numero entero "))
print (f"""{numero} * 0 = {numero*0} 
{numero} * 1 = {numero*1}
{numero} * 2 = {numero*2}
{numero} * 3 = {numero*3}
{numero} * 4 = {numero*4}
{numero} * 5 = {numero*5}
{numero} * 6 = {numero*6}
{numero} * 7 = {numero*7}
{numero} * 8 = {numero*8}
{numero} * 9 = {numero*9} 
{numero} * 10 = {numero*10} """)

#Ejercicio 7

num1 = float(input(" Ingrese un numero distinto de 0: "))
num2 = float(input(" Ingrese otro numero distinto de 0: "))

suma = num1 + num2
resta = num1 - num2
division = num1 / num2
multiplic = num1 * num2

print(f"""
      la suma de ambos numeros es: {suma}
      la resta entre ellos es: {resta}
      dividirlos da como resultado: {division}
      y multiplicarlos da: {multiplic}""")

#Ejercicio 8

altura = float(input( " Ingrese su altura en metros "))
peso = float(input(" Ingrese su peso en kilogramos "))

imc = peso / (altura**2)

print(f" Su indice de masa corporal es {imc}")

#Ejercicio 9

celsius = float(input(" Ingrese una temperatura en grados Celsius "))

fahren = ((9/5)*celsius) + 32

print(f" Su equivalente en grados fahrenheit es de : {fahren}")

#Ejercicio 10

num1 = float(input(" Ingrese el primer numero "))
num2 = float(input(" Ingrese el segundo numero "))
num3 = float(input(" Ingrese el tercer numero "))

promedio = (num1+num2+num3) / 3

print(f" El promedio entre esos tres numeros es : {promedio}")
