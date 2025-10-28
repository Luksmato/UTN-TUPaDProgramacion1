# Crear una lista con las notas de 10 estudiantes
# Mostrar la lista completa.
# Calcular y mostrar el promedio.
# Indicar la nota más alta y la más baja.

notas = [8.5, 9, 7, 9, 8, 7.5, 9.5, 5, 4, 6]   
for nota in notas:
    print(nota)


promedio = sum(notas) / len(notas)
print("Promedio de notas:", promedio)

nota_mas_alta = max(notas)  
nota_mas_baja = min(notas) 

print("Nota más alta:", nota_mas_alta)  
print("Nota más baja:", nota_mas_baja)

