# Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# Calcular el promedio de las mínimas y el de las máximas.
# Mostrar en qué día se registró la mayor amplitud térmica.

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temperaturas = [[15, 25], [15, 28], [16, 22], [13, 30], [18, 30], [20, 32], [22, 29]]

suma_min = 0
suma_max = 0    

for temp in temperaturas:
    suma_min += temp[0]
    suma_max += temp[1]
promedio_min = suma_min / len(temperaturas)
promedio_max = suma_max / len(temperaturas)
print("Promedio de temperaturas mínimas:", promedio_min)
print("Promedio de temperaturas máximas:", promedio_max)

mayor_amplitud = 0
dia_mayor_amplitud = ""
for i in range(len(temperaturas)):
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = dias[i]

print("Día con mayor amplitud térmica:", dia_mayor_amplitud)
print("Amplitud térmica:", mayor_amplitud)

