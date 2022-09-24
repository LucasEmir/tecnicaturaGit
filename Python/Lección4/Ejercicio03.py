# Ejercicio 03: Incertar elementos y ordenarlos
# Pedir números y meterlos en una lista, cuando el usuario
# introduzca un número 0, nuestro programa dejaría de incertar.
# Por último, mostrar los numeros ordemados de menor a mayor

lista = []
salir = False
while not salir:
    numero = int(input('Digite un número: '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort() #La lista esta ordenada con esta función
print(f'\n Lista ordenada: \n{lista}')


