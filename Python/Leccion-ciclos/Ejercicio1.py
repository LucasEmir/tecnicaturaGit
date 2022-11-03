#Ejercicio 1
#Calular la suma de "N" números primos.

n = int(input('Dígite la cantidad de números a sumar: '))
suma = 0
for i in range(1,n + 1):
    num = int(input('Ingrese un número a sumar: '))
    suma += num
else:
    print(f'El resultado de la suma es: {suma} ')
