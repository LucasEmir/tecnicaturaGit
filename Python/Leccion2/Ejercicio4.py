# Etapas de la vida según la edad
edad = int(input('Digite su edad: '))
mensaje = None
if 0 <= edad < 10: #Sintaxis simplificada
    mensaje = 'La infancia es increible y bella'
elif 10 <= edad < 20:
    mensaje = 'Tienes muchos cambios, mucho que estudiar'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo'
elif 30 <= edad < 40:
    mensaje = 'Más trabajo y responsabilidades'
elif 40 <= edad < 50:
    mensaje = 'Falta menos para la jubilación'
else:
    mensaje = 'Error etapa de vida no reconocida'
print(f'Tu edad es:  {edad}, {mensaje}')
