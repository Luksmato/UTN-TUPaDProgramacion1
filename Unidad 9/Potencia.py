# Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛
# 𝑚 = 𝑛 ∗ 𝑛 (𝑚−1). Prueba esta función en un algoritmo general.

def potencia (base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia (base, exponente - 1)
    
base = int(input(" Ingrese el numero base: "))
exponente = int(input( " INgrese el exponente: "))
resultado = potencia (base, exponente)

print (f" El resultado de {base} elevado a la {exponente} es: {resultado}")

