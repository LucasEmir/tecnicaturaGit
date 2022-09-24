# Ejercicio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga dos listas y que a continuación
# Cree las siguientes listas (en las que no debe haber repetición)
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista pero no en la segunda
# 3 Lista de palabras que aparecen en la segunda lista pero mo en la primera
# 4 Lista de palabras que aparecen en ambas listas

nombres1 = ['Argentina', 'Mexico', 'Canada', 'Argentina', 'Mexico', 'Canada', 'EEUU', 'Camerun', 'Holanda']
nombres2 = ['Argentina', 'Mexico', 'Canada', 'EEUU', 'Turquia', 'España', 'EEUU', 'Turquia', 'España']

#Eliminar los elementos repetidos de ambas listas con conjuntos
conjunto1 = set(nombres1)
conjunto2 = set(nombres2)

union = list(conjunto1 | conjunto2) #Unimos los dos conjuntos
solo1 = list(conjunto1 - conjunto2) #Solo muestra el conjunto 1
solo2 = list(conjunto2 - conjunto1) #Solo muestra el conjunto 2
interseccion = list(conjunto1 & conjunto2) #MOstramos ambas listas


print(f"Lista de palabras que aparecen en las listas: {union}")
print(f"Lista de palabras que aparecen en la primera lista pero no en la segunda: {solo1}")
print(f"Lista de palabras que aparecen en la segunda lista pero mo en la primera: {solo2}")
print(f"Lista de palabras que aparecen en ambas listas: {interseccion}")
