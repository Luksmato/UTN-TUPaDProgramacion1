# Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# Inicializarlo con guiones "-" representando casillas vacías.
# Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# Mostrar el tablero después de cada jugada.

tablero = []

for i in range(3):
    fila = []
    for j in range(3):
        fila.append("-")
    tablero.append(fila)

for fila in tablero:
        for celda in fila:
            print(celda, end=" ")
        print()

jugador= "X"
turno= 0

while turno < 9:
   
    print(f"Turno del jugador {jugador}")
    
    fila = int(input("Ingrese la fila (1, 2, 3): ")) -1
    columna = int(input("Ingrese la columna (1, 2, 3): ")) -1

    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("Posición inválida. Intente de nuevo.")
        continue
    
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
        turno += 1
    else:
        print("Casilla ya ocupada. Intente de nuevo.")
        continue

    for fila in tablero:
        for celda in fila:
            print(celda, end=" ")
        print()

    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"









