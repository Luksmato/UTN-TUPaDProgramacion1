# Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Ejemplo:
# agenda = { ("lunes","10:00"): "Reunion", ("martes","15:00"): "Clase de Ingles" }
# Permití consultar qué actividad hay en cierto día y hora.

agenda = { ("lunes","19:00"): "Turno Doctor", ("martes","11:00"): "Reunion Trabajo", ("miercoles","14:30"): "Clase de Paddle", ("jueves","09:00"): "Entrega Proyecto"}

def consultar_evento(dia, hora):
    clave = (dia, hora)
    if clave in agenda:
        return agenda[clave]
    else:
        return "No hay eventos programados en ese día y hora."
    
while True:
    print("\nConsultar evento en la agenda")
    dia = input("Ingrese el día: ")
    hora = input("Ingrese la hora (formato HH:MM): ")
    evento = consultar_evento(dia, hora)
    print(f"Evento en {dia} a las {hora}: {evento}")
    

