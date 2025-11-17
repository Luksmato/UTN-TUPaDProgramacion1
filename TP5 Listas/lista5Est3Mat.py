# Crear una matriz con las notas de 5 estudiantes en 3 materias.
# Mostrar el promedio de cada estudiante.
# Mostrar el promedio de cada materia.

notas = [ [8, 9, 7], [8.5, 6, 9], [6, 5, 8], [7, 8, 7], [10, 8, 9] ]

for i in range(len(notas)):
    promedio_estudiante = sum(notas[i]) / len(notas[i])
    print(f"Promedio del estudiante {i+1}: {promedio_estudiante}")

for j in range(len(notas[0])):
    suma_materia = sum(notas[i][j] for i in range(len(notas)))
    promedio_materia = suma_materia / len(notas)
    print(f"Promedio de la materia {j+1}: {promedio_materia}")

