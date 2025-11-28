# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def Fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
    
num = int(input(" Ingrese la posición hasta donde quiere ver la serie de Fibonacci: "))

print (f"Serie de Fibonacci hasta la posición {num}:")
for i in range(num + 1):
    print(Fibonacci(i)) 


