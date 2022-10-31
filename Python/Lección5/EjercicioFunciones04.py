# Ejercicio 4: Crear una calculadora de Impuestos (Video 7.6)
# Crear una función para calcular el total de un pago incluyendo
# un impuesto aplicado. (IVA)
# Foemula: pago_total = pago_sin_impuesto + pago_sin_impueston* (impuesto/100)
# Proporcione el pago sin impuesto: 1000
# Proporcione el monto del impuesto: 21%
# Pago con impuesto: xxxxx


# Creamos la función que calcula el total del pago incluyendo el impuesto
def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

# Ejecutamos la función
pago_sin_impuesto = float(input('Digit el pago sin impuesto: '))
impuesto = float(input('Digite el monto del impuesto a alicar: '))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'El pago con impuesto es: {pago_con_impuesto}')
