miVariable = 3
print(miVariable)
miVariable = "Hola a todos los estudiantes de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
# Las literales se escriben x240, la variable y = x984, la variable z =x304
print(id(y))
print(id(z))

# Tipos int, float, String, Bool
X = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas
miGrupoFavorita = "Jorge Drexler"
caracteristicas = "Mejor artista uruguayo"
print("Mi grupo favorito es:", caracteristicas, miGrupoFavorita)

#numero1 = "7"
#numero2 = "8"
#print(int(numero1) + int(numero2))

# Tipos Boleanos (bool)
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar entrada del usuario
# Funcion input
#resultado = input("Digite un número: ")  # regresa un dato de tipo String
#print(resultado)

# Conversión de la entrada de datos
numero1 = int(input("Escribe el primer número: "))
numero2 = int(input("Escribe el segundo número: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)

# Ejercicio 1
dia = int(input("¿Cómo estuvo tu día: "))
print(dia)
print("Mi día estuvo de ", dia)

# Ejercicio 2
titulo = input("Proporciona el título del libro: ")
autor = input("proporciona el nombre del autor. ")
print("el", titulo, "fue escrito por", autor)

