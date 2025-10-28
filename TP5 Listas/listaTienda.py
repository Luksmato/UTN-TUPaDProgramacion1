# Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# Mostrar el total vendido por cada producto.
# Mostrar el día con mayores ventas totales.
# Indicar cuál fue el producto más vendido en la semana.

productos = ["Producto A", "Producto B", "Producto C", "Producto D"]
ventas = [[15, 20, 23, 30, 31, 8, 12],
        [10, 15, 6, 25, 30, 7, 40],  
        [20, 25, 19, 38, 49, 45, 51],
        [52, 18, 15, 14, 26, 28, 38]]

total_por_producto = [0] * len(productos)
total_por_dia = [0] * len(ventas[0])

for i in range(len(productos)):
    for j in range(len(ventas[0])):
        total_por_producto[i] += ventas[i][j]
        total_por_dia[j] += ventas[i][j]
    print(f"Total vendido del {productos[i]}: {total_por_producto[i]} unidades")
dia_mayor_venta = total_por_dia.index(max(total_por_dia)) + 1

print(f"Día con mayores ventas totales: Día {dia_mayor_venta} con {max(total_por_dia)} unidades vendidas")
producto_mas_vendido = total_por_producto.index(max(total_por_producto))
print(f"Producto más vendido en la semana: {productos[producto_mas_vendido]} con {max(total_por_producto)} unidades vendidas") 

      
