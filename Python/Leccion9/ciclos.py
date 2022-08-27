#Año bisiesto
print('Comprobamos que el año es bisiesto')

opcion = 0
while opcion != 1:
    año = int(input('Ingrese el año: '))
    if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
        print(f'El año ,{año}, es bisiesto')
    else:
        print(f'El año ,{año},no es bisiesto')
    opcion = int(input('Para seguir adelante digite la opción 1 '))

