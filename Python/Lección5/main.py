# Comenzamos con funciones
# mi_funcion() no se puede llamar antes de ser definida
# Definimos una función
def mi_funcion ():
    print('Hola a todos')
    print('Respetando la tabulación podemos ingresar muchas cosas')
#print('ejemplo') # Esto ya estaria fuera de la función porque perdio la identación

mi_funcion() # Estamos llamando a la función
mi_funcion() # Se puede llamar a la funcion N cantidad de veces

#Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+' '+lastName)
person = ["Ariel", "Betancud"]
show(person[0], person[1]) #Pasamos uno por uno los datos de las listas a la función
show(*person) #Esto es lo mismo que lo anterior pero pasamos todo junto
person2 = ('Osvaldo', 'Giordanini') # Desempaquetamos a través de una tupla
show(*person2)
person3 = {"lasName": "Lucero", "name": "Natalia"}
show(**person3)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
else:  #La única forma para que no se ejecute el else es con un condicional y un break(ej video)
    print('Esto se termino.')

# List comprehension, lista de conprencion

names = {"Paolo", "Rodrigo", "Lupe", "Pepe"}
alongP = [p for p in names if p[0] == 'P'] #Esto regresa una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "Country": "Arg"},
            {"name": "corona", "Country": "Mex"},
            {"name": "Bud", "Country": "EEUU"}]
Arg = [b for b in bottleC if b["Country"]] == "Arg"
print(Arg)
print(bottleC)
# Paso de argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos")
    print(f'Nombre: {name}, "Apellido: {lastName}')

mi_funcion2('Jorge','Pepe')
mi_funcion2('Juan','Cacho')
mi_funcion2('Nora','Juana')

#  La palabra retur en funciones
# Creamos una función para sumar
def sumar(a, b):
    return a + b
resultado = sumar(78, 22)
print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(50 , 45)}') #Llamamos a la funcion directamente desde el print

def sumar2(a = 0, b = 0): # Le damos un valor por default
    return a + b
resultado1 = sumar2()
print(f'Resultado de la suma: {sumar2()}')
print(f'Resultado de la suma: {sumar2(22, 66)}') #Moficamos el valor asignado por default

# Argumentos, variables en funciones
def listarNombres(*nombres):#Cuando no sabemos cuantos argumentos recibira (*args se utiliza generalmente)
    for nombre in nombres: # Se va a convertir en tupla
        print(nombre)
listarNombres('Pepe', 'Juan', 'Jose', 'Ignacio') #Llamado a la función y paso por parámetro
listarNombres('lele', 'lala', 'David', 'Lolo')

#7.2 Argumentos variables para un diccionario
def listarTerminos(**terminos): #Lo más utilizado es **kwargs par recebir los argumentos
    for llave, valor in terminos.items(): # Kwargs significa: key word argument
        print(f'{llave} : {valor}')

listarTerminos() # No recibe nada, nada se va a mostrar
listarTerminos(IDE='Integrated Develoment Eviroment', PK='Primary Key')
listarTerminos(Nombre='Leonel Messi')

#7.3 Lista de elementos con funciones convertir
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito', 'Pedro','Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
#desplegarNombres(10, 11) Esto no es un objeto iterable
desplegarNombres((10, 11)) #Esto es una tupla, si es iterable
desplegarNombres([22, 55]) #Lo convertimos en una lista

#7.4 Funciones recursivas 

def factorial(numero):
    if numero == 1: # Caso base
        return 1
    else:
        return numero * factorial(numero-1) #Caso recursivo

resultado = factorial(5) # Lo hacemos en código duro
print(f'El factorial del número 5 es: {resultado}')



def factorial1(numero1):
    if numero1 == 1: # Caso base
        return 1
    else:
        return numero1 * factorial(numero1-1) #Caso recursivo

resultado1 = factorial1(numero1= int(input('Ingrese un número: ')))
print(f'El factorial del número ingresado es: {resultado}')

