# lista = Ariel , liliana, Natalia, Osvaldo
"""
video 1
nombres = ['Naty', 'Osvaldo', 'Lili', 'Ariel']
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])
"""

#video 2
nombres = ['Naty', 'Osvaldo', 'Lili', 'Ariel']
print(nombres)
print(nombres[0:2]) # solo muestra el indice 0,1 pero no el indice 2
#ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) #Indices a mostrar 0, 1, 2
#Desde el indice indicado hasta el final
print(nombres[1: ])
#Modificamos un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)
#Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# Video 3
# Preguntamos cuantos elementos tiene una lista
print(len(nombres)) #le pasamos como parámetros la lista

# Agregar elementos
nombres.append('Marcelo')

# Incertar un elemento en un indoce específico
nombres.insert(1,'Alberto')
print(nombres)
nombres.insert(3,'Debora')
print(nombres)

# Eliminamod un elemento
nombres.remove('Alberto')
print(nombres)

# Eliminar el último elento
nombres.pop()
print(nombres)

# Eliminar un indice específico
del nombres[2] # del significa delete (eliminar)
print(nombres)

# Eliminar todos los elementos de la lista
nombres.clear()
print(nombres)

"""
# Eliminar la lista
del nombres
print(nombres) # Nos va a motrar un error
"""
# Video 4 "tuplas"
# Definir tupla
cocina = ('cuchara' , 'cuchillo','tenedor')
print(len(cocina))

# Acceder a un elemento, utilizamos corchetes, no parentesis
print(cocina[0])
print(cocina[-1])

# Acceder a un rango
print(cocina[0:1]) # Nos muestra la coma final
# Ejemplo
verduras = ('papa') # Esto es un String, al imprimirlo no muestra la coma final.

# Video 5
# Recorremos los elementos de una tupla
for cocinar in cocina: # Print esta usando \n para saltos de linea
    print(cocinar, end =' ') # Usamos end= para eliminar los saltos de linea

# La unica forma de modificar una tupla es con convercion (No recomendado dentro de las buenas practicas)
cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n',cocina)

# Eliminar la tupla
del cocina
print(cocina)

