#Ejercicio 6: Tabla de multiplicar
# Hacer un programa quee pida un número por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10. Por ej:
# Si digita el 5 l alista tendrá: 5 10, 15, 20, 25, 30, 35, 40,45, 50

numero = int(input("Digite un número: "))
lista = [] #Creamos una lista vacia
for i in range(1,11):
    lista.append(i*numero)
print(f'\nTabla de multiplicar del {numero}: \n {lista}')

lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for indice, i in enumerate(lista2):
    print(f'{numero} x {i} = {lista[indice]}')
