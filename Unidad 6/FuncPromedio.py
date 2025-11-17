# Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio (a, b, c):
    promedio = (a + b + c) / 3
    return promedio

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

resultado_promedio = calcular_promedio(num1, num2, num3)
print(f" El promedio de {num1}, {num2} y {num3} es: {resultado_promedio:.2f} ")