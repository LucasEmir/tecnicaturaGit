# Ejercicio 4
# Calificaciones

calificacionBaja = 99999
suma = 0
i = 1
for i in range(10):
    calificacion = int(input('Ingrese una calificación: '))
    suma = suma + calificacion
    if calificacion < calificacionBaja:
        calificacionBaja = calificacion
calificacionPromedio = suma / 10

print(f'La calificación promedio es: {calificacionPromedio}')
print(f'La calificación más naja es: {calificacionBaja}')
