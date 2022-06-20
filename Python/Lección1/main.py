'''
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
'''
"""
operadorA = 8
operadorB = 5
suma = operadorA + operadorB
#print("Resultado de la suma: ", suma)
print(f'El resultado de la suma es: {suma}') #Esto es interpolación

resta = operadorA - operadorB
print(f'El resultado de la resta es:  {resta}')


multiplicacion = operadorA * operadorB
print(f"El resultado de la multiplicación es:  {multiplicacion}")

division = operadorA / operadorB
print(f"el resultado de la división es: {division}")
division = operadorA // operadorB
print(f"El resultado de la división (int) es: {division}")
modulo = operadorA % operadorB
print(f"El resultado de división o residuo es: {modulo}")
exponente = operadorA ** operadorB
print(f"El resultado del exponente es: {exponente}")

# Ejercicio rectangulo
alto = int(input("Por favor ingrese el alto. "))
ancho = int(input("Por favor ingrese el ancho. "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print(f"El area es: {area}")
print(f"El perímetro es: {perimetro}")

miVariable3 = 10
print(miVariable3)

# Operadores de reasignación
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# miVariable3 = miVariable - 2
miVariable3 -= 2
print(miVariable3)

# miVariable3 = miVariable * 3
miVariable3 *= 3
print(miVariable3)

# miVariable3 = miVariable / 2
miVariable3 /= 2
print(miVariable3)

# Operadores de comparación

d = 4
b = 2
resultado = d == b  # Comparamos si son iguales
print(resultado)

# Operador diferente
resultado = d != b
print(resultado)

# Operador mayor que
resultado = d > b
print(resultado)

# Operador menor que
resultado = d < b
print(resultado)

# Operador menor o igual que
resultado = d <= b
print(resultado)

# Operador mayor o igual que
resultado= d >= b
print(resultado)

a = int(input("Ingrese un número: "))
print(f"El residuo de la división es: {a % 2}")
if a % 2 == 0:
    print(f"El valor de a es : {a} es número PAR")
else:
    print(f"El valor de a es: {a} es número Impar")
"""
"""
edadAdulto = 18
edadPersona = int(input("Ingresar tu edad: "))
if edadPersona >= edadAdulto:
    print(f"Su edad es: {edadPersona} años, usted es mayor de edad.")
else:
    print(f"Su edad es: {edadPersona} años, usted es menor de edad")
"""
"""
# Operadores Lógicos

a = False
b = True
resultado = a and b
print(resultado)

# Operador or
resultado = a or b
print(resultado)

# Operador not
resultado = not a
print(resultado)
"""
"""
# Ejercicio: Valor dentro de un rango
valor = int(input("Digite un número dentro del rango 0 a 5: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = (valor >= valorMinimo and valor <= valorMaximo)
if dentroRango:
    print(f"El valor {valor} esta dentro del rango")
else:
    print(f"El valor {valor} no esta dentro del rango")
"""
"""
# Ejercicio con el operador or, Operador not
vacaciones = False
diaDescanso = True
if not (vacaciones or diaDescanso):
    print("Puede asistir al juego")
else:
    print("Tiene trabajo que hacer")
"""
# Ejercicio: Rango entre 20 y 30 años
#edad = int(input("Digite su edad: "))
# veinte = edad >= 20 and edad < 30
# print(veinte)
# treinta = edad >= 30 and edad < 40
# print(treinta)
"""
# if veinte or treinta:
if (20 <= edad <30) or (30 <= edad < 40): # Sintaxis simplificada del operador and
    print("Estas dentro del rango de los (20'0)a (30'0) años")
#    if veinte:
#       print("Esta dentro del rango de los (20\'0) a (30\'0) años")
#    elif treinta:
#        print("Estas dentro del rango de los (20\'0) años")
#    else:
#        print("No estas dentro del rango")
else:
    print("No esta dentro del rango de los (20\'0) a (30\'0) años")

# Ejercicio: El mayor de dos números
numero1 = int(input('Digite el valor para número1 '))
numero2 = int(input('Digite el valor para numero2 '))

if numero1 > numero2:
    print('Número 1 es mayor')
else:
    print('Número dos es mayor')

# Ejercicio: Tienda de libros
print("Digite los digientes datros del libro")
nombre = input("Digite el nombre del libro: ")
id = int(input("Digite el ID del libro: "))
precio = float(input("Digite el precio del libro: "))
envioGratuito = input("Indicar si el libro es gratuito(True/False): ")
if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "El valor es incorrecto, debe escribir True/False"
print(f'''
        Nombre: {nombre}
        Id: {id}
        Precio: {precio}
        Envio Gratuito?: {envioGratuito}
''')
"""
