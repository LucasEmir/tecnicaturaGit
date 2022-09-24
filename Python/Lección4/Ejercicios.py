seleccionArgentina = {
    10: {'Nonmbre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posición': 'Extremo derecho'},
    11: {'Nonmbre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posición': 'Extremo derecho'},
    21: {'Nonmbre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posición': 'Media Punta'},
    19: {'Nonmbre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posición': 'Defensor Central'},
    1: {'Nonmbre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posición': 'Portero'},
    22: {'Nonmbre': 'Lautaro Martinez', 'Edad': 25, 'Altura': 1.74, 'Precio': '106 Millones', 'Posición': 'Delantero'},
    23: {'Nonmbre': 'Emiliano Martinez', 'Edad': 29, 'Altura': 1.95, 'Precio': '22 Millones', 'Posición': 'Portero'},
    25: {'Nonmbre': 'Alejandro Papu Gomez', 'Edad': 34, 'Altura': 1.67, 'Precio': '7.5 Millones', 'Posición': 'Centrocampista'},
    5: {'Nonmbre': 'Leandro Paredes', 'Edad': 28, 'Altura': 1.80, 'Precio': '7 Millones', 'Posición': 'Centrocampista'}
}
for llave, valor in seleccionArgentina.items():
    print(llave, valor)
print('Tenemos cargados en el diccionario la cantidad de jugadores: ', end= ' ')
print(len(seleccionArgentina))

#En los videos esta como ejercicio 5 (Solo enseña ortra forma de recorrer con el bucle for)

for i in seleccionArgentina:
    print(f'{i} ->{seleccionArgentina[i]}')


