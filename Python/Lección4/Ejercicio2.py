# Ejercicio 2: Nodificar los elementos de una lista
# Llenar una lista con los números del 1 al 10, luego modificar los
# elementos de una lista multiplicandolos por un valor ingresado por el usuario

lista = list(range(1, 11))
print('Lista Original')
for i in lista:
    print(i, end='_')
ingreso = int(input('\nIngrese un número: '))
# Multiplicamos todos los elementos de la lista
for indice, i in enumerate(lista):
    lista[indice] *= ingreso

print(f'Lista final con los elementos multiplicados por {ingreso}')
for i in lista:
    print(i, end=' ')
