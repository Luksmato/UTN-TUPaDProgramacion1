# Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1 = {4, 7, 10, 5, 6, 8, 3}
parcial_2 = {1, 2, 4, 5, 9, 7}


aprobados_ambos = parcial_1.intersection(parcial_2) 
print("Estudiantes que aprobaron ambos parciales:", aprobados_ambos)

aprobados_solo_uno = parcial_1.symmetric_difference(parcial_2)  
print("Estudiantes que aprobaron solo uno de los dos parciales:", aprobados_solo_uno)   

aprobados_al_menos_uno = parcial_1.union(parcial_2)
print("Estudiantes que aprobaron al menos un parcial:", aprobados_al_menos_uno)



