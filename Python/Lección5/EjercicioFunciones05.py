# Ejercicio 5: Convertidor de temperaturas (7.7)
# Realizar dos funciones para convertir de grados celcius
# a fahrenheit y viceversa.
# Investigar las formulas

# Función que convierte de celcius a fahrenheit
def celsius_fahrenheit(celcius):
    return celcius * 9 / 5 + 32 # La precedencia: multiplicación, divisón y suma

# Funcion que convierte fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 # Respeta la procedencia utilizando parentesis

celsius = float(input('Digite el valor de celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} C a F -> {resultado:.2f}')

fahrenheit = float(input('Digite el valor de fahrenheit: '))
resultado =  fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a <c -> {resultado:.2f}')
