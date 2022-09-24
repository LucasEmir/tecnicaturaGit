# Ejercicio 1: Eliminar duplicados en una  lista
# Escriba un programa donde tenga una lista y que a continuación
# Elimine los elementos repetidos, por último mostrar la lista

#Creamos la lista
nombresPais = ['Argentina', 'Mexico', 'Canada', 'EEUU', 'Mexico', 'Canada']
print(nombresPais)
conjunto = set(nombresPais) #Convertinos la lista a un conjunto de tipo set
nombresPais = list(conjunto) #Convertimos el conjunto a un lista
# nombresPais = list(set(nombresPais)) Conversión hecha en una sola linea de código
print(nombresPais)


