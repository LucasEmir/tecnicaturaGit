# Ejercicio 3: Función recursiva (Video 7.5)
# Imprimir números de 5 a 1 de manera descendente usando funciones recursivas
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el
# valor de 5, debe imprimir:
# 5
# 4
# 3
# 2
# 1
# En caso de ser número 3 debe imprimir:
# 3
# 2
# 1
# Si ingresa números negativos no imprime nada

def imprimir_numeros_recursivos(numero):
    if numero >= 1:
        print(numero)
        imprimir_numeros_recursivos(numero-1) #Caso recursivo
    elif numero == 0:
        return # se coloca el retorno vacio para evitar errores
    elif numero <= 0:
        print('El valor ingresado es incorrecto...')

# imprimir_numeros_recursivos(5)

imprimir_numeros_recursivos(int(input('ingrese un número positivo por favor. ')))
