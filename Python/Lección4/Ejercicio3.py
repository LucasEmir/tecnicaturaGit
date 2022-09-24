#Ejercicio 3: Insertar elementos ordenados
#Pedir números y meterlos en una lista, cuando el usuario


lista = []
salir = False
while not salir:
    numero = int(input('Digite un número:  '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort() # La lista esta ordenada con la función sort
print(f'\nLista ordenada: \n{lista}')
