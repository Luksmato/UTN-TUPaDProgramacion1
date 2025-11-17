# Crear una lista con los nombres de 8 estudiantes presentes en clase.
# Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# Mostrar la lista final actualizada.

estudiantes = ["Olivia", "Sole", "Matias", "German", "Silvia", "Silvana", "Chris", "Maximiliano"]

for estudiante in estudiantes:
    print(estudiante)

print("¿Desea agregar un nuevo estudiante (A) o eliminar uno existente (E)?")
opcion = input("Ingrese A para agregar o E para eliminar: ").upper()    

if opcion == 'A':
    nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo_estudiante)
    print(f"{nuevo_estudiante} ha sido agregado a la lista.")
elif opcion == 'E':
    estudiante_a_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if estudiante_a_eliminar in estudiantes:
        estudiantes.remove(estudiante_a_eliminar)
        print(f"{estudiante_a_eliminar} ha sido eliminado de la lista.")
    else:
        print(f"{estudiante_a_eliminar} no se encuentra en la lista.")
else:
    print("Opción no válida.")

print("Lista final de estudiantes:")
for estudiante in estudiantes:
    print(estudiante)

