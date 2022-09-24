import math
# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8) #Definimos la tupla
# Crear una lista que solo incluya los números menores a 5
# e imprima por consola [1, 3, 2]

lista = [] # Definimos la lista
#Filtramos los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

#Ejercicio de matematicas
#Para sacar la raíz cuadrada de un número

numero = int(input('Digite un número positivo: '))
while numero < 0:
    print("Error -> Debería ser un número positivo.")
    numero = int(input('Digite un número positivo: '))
print(f'\nSu raiz cuadrada es: {math.sqrt(numero):.2f}') #2f es para que el resultado solo muestre dos números