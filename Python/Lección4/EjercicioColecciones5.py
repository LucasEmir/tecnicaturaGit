# Ejercicio 5:Factorial de un número positivo
# Hacer un programa para calcular el factorial de un número positivo

numero = int(input('Digite un numero: '))
while numero < 0: # Mientras que el número sea negativo
    print('Error -> el número tiene que ser positivo.')
    numero = int(input('Digite un número: '))
factorial = 1 # Variable para calcular el factorial
for i in range(1, numero+1):
    factorial *=i
    print(f'\nEl factorial del numero {numero} positivo ingresado es:{factorial}')
