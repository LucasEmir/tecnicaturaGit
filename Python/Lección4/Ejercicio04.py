# Ejercicio 4: Sumar números pares dentro de un rango
# Hacer un programa para sumar números pares dentor de una rango, por ejemplo
#                       suma de números pares del 2 al 30
#                       suma = 240

a = int(input("Digite donde comenzará la suma: "))
b = int(input("Digite hasta donde quiere llegar a sumar: "))
suma = 0
for i in range(a,b+1):
    if i%2 == 0: #Esto nos dice si el número es par
        suma += i
print(f'\nLa suma de números pares dentro del rango es: {suma}')
