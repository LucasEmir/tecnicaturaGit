#Ejercicio 4: Sumar números pares dentro de un rango
#Hacer un programa para sumar números pares dentro de un rango,
#por ejemplo:
#               suma de números pares del 2 al 30
#               suma = 240

a = int(input('Diite de donde comenzará la suma: '))
b = int(input('Digíte hasta donde quiere llegar con la suma: '))
suma = 0
for i in range(a,b+1):
    if i % 2 == 0: # Esto es si el número es par
        suma += 1
print('\nLa suma en rango es: ',{suma})

