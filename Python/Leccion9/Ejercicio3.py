# Ejercicio 3
# Leer diez números e imprimir cuantos son positivos, cuantos negativos y cuantos neutros.

numNeutro = 0
numPositivo = 0
numNegativo = 0

for i in range(10):
    num1 = int(input('Dígite un número: '))
    if num1 == 0:
        numNeutro = numNeutro + 1
    else:
        if num1 < 0:
            numNegativo = numNegativo + 1
        else:
            numPositivo = numPositivo + 1

print(f'Los números neutros son: {numNeutro}')
print(f'Los números negativos son: {numNegativo}')
print(f'Los números positivos son: {numPositivo}')
