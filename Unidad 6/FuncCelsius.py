# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit.
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
  
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

temp_celsius = float(input("Introduce la temperatura en grados Celsius (°C): "))

temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)

print(f"{temp_celsius:.2f} °C son equivalentes a {temp_fahrenheit:.2f} °F.")
