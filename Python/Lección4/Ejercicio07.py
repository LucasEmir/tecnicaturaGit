# Ejercicio 7: Juego adivina el número
# Realizar un juego para adivinar un  número. Para ello se debe
# generar un número aleatorio entre 1 -100, y luego ir pidiendo
# números indicando "es mayor" o "es menor" según sea mayor o menor
# con respecto a N. El proceso termina cuando el usuario acierta
# y allí debe mostrar el número de intentos.

import random
print("\t.:Juego adivina el número:.")
aleatorio = random.randint(0,100) # Toma de 0 a 100 literal, generamos un número aleatorio
contador = 0
while True:
    numero = int(input("Digite un número: "))
    contador += 1
    if numero > aleatorio:
        print("\tNo es el número, digite un número menor")
    elif numero < aleatorio:
        print("\tNo es el número, digite un número mayor")
    else:
        print(f"Felcidades acabas de adivinar el número {aleatorio}")
        break #Rompe el ciclo y el bucle
print(f"\nNúmero de intentos: {contador}")
