# lista = Ariel , liliana, Natalia, Osvaldo
#Colecciones en Python
#Las listas se conocen en otros lenguajes como arreglos o vectores
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
#Puede contener otro tipo de datos, incluso otra lista
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
print(nombres)
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
#del cocina
print(cocina)
#####################################################################################################
#Clase 2
#Video 1
#Tipo set
planetas = {'Marte', 'Júpiter', 'Venus'} #Los ordena aleatoriamente, lo comprobamos al imprimir
print(planetas)
print(len(planetas)) # nos indica el largo con len

#Revisamos si un elemento existe dentro de un set
print('Marte' in planetas) # responde con un booleano

# Agregar un elemento
planetas.add('Tierra') # Add es una función, no se pueden agregar elementos duplicados
print(planetas)

# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Júpiter') #Esta función ante un mal ingreso u inexixtencia del elemento da error
print(planetas)
planetas.discard('Tierra') #Esta función no nos presenta nungún error
print(planetas)

#Video 2
#Limpiar set o conjuntos
planetas.clear()
print(planetas)

#Eliminar set o conjuntos
del planetas
#print(planetas)

#Video 3
#Diccionarios
# 'Maradona':10 Un diccionario esta compuesto pot dos elementos.
# UNA LLAVE Y UN VALOR
# dict(key, value)
diccionario = {
    'IDE':'Integrated Development Enviroment',
    'POO':'Programación Orientada a Objetos',
    'SABD':'Sistema de Administración de Base de Datos'
}
#verificar la cntidad de elementos de un diccionario
print(len(diccionario))
print(diccionario)
#Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

#Otra forma de recupear un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

#Modificar los elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

#Video 4
# Como recorrer los elementos
for termino in diccionario:#recorremos mostrando solo las llaves
    print(termino)

#Necesitamos una función para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino,valor)

#Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino)#Muestra solo las llaves

for valor in diccionario.values():
    print(valor)

#Comprobar la existencia de algun elemento
print('IDE'in diccionario) #Nos devuelve un valor boleano

#Agregar un elemento a nuestro diccionario
diccionario['PK'] = 'Primary Key'
print(diccionario)

#Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar un diccionario
del diccionario #El diccionario se borro

#Video 4 era de repaso
#Video 5

#Concatenamos listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1+lista2
print(lista3)

lista3.extend([7, 8, 9])#Función para agregar varios elementos
print(lista3)

print(lista3.index(5)) #Función para ver en que posiciín se encuentra el elemento ingresado

#Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1))# Pasamos el valor buscado
#print(lista3.count(0)) Esto nos daría un error por no ser el elemento parte de la lista

#Para poner la lista al reves
lista3.reverse()
print(lista3)

#Video6
#Para que una lista se multiplique repitiendo sus elementos
lista = [1, 2, 3] * 2
print(lista)

#Metodos de ordenamiento
lista3.sort() #Los ordena ascendentemente
print(lista3)
lista3.sort(reverse=True)
print(lista3) #Los ordena descendentemente

#Video 7
#Repaso de tuplas
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola') # Puede tener diferente tipos de datos dentro
print(tupla)

print(4 in tupla) #Acción booleana, pregunta su se encuentra un elemento en la tupla

######################################################################################################
# Clase 3
#video 1
# Repaso de set o conjunto
# Para definir un conjunto
conjunto2 = set() # Con set se puede inicializar vacio
conjunto1 = {'bye', } # Si usamos llaves no podemos inicializarlo vacio
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('hola')
print(conjunto1)
print(3 not in conjunto1) # Preguntamos si el número 3 No esta en el conjunto 1

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) #Nos devuelve un booleno

#Video 2
#"Operaciones en conjuntos"
conjunto3 = conjunto1 | conjunto2 # La línea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Que elemento tienen en común
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 #Asigna el valor que está en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1

conjunto3 = conjunto1 ^ conjunto2 # Elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

#Video 3

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # Aquí preguntamos si un conjunto es subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Preguntamos si los elementos del conjunto uno están  dentro del cojunto 3
print(conjunto3.issuperset(conjunto2)) # Si es verdadero quiere decir que el conjunto3 es un super conjunto
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto es si coparten elementos en común
print(conjunto1.isdisjoint(conjunto2)) # En este ejemplo no hay cosas en común

# Convertir un conjunto en inmutable
# No se puede agregar, modificar ni eleminar elementos del conjunto
conjunto1 = frozenset # Esto hace que el conjunto sea totalmente inmutable

#Video 4
# Repaso diccionarios
diccionarioNuevo = { 'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)

# Como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipios de datos
diccionario2 = {'Ariel': {'Edad': 40, 'Altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia': [35, 1.67]}
print(diccionario2)

#Video 5 (3.3)
#Lo hice en los ejercicios

#Video 6 (3.4)
#Pilas usando las listas
pila = [1, 2, 3]

#Agregar lementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop() #Quitamos el último elemento y lo guardamos en una variable
print(f'sacamos el elemento {elementoBorrado}')
print(f'La pila ahora quedo así{pila}')

# Video 7 (3.5)
# Colas con listas
# Estructura de datos de tipo fifo(firs input / first output)
cola = ['Ariel', 'Osvaldo', 'Liliana','Pilar']

#Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('Jose')
print(cola)

#Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Se retira el cliente: {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Se retira el cliente: {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Se retira el cliente: {seRetira}')
print(cola)

########################################################################################################
















