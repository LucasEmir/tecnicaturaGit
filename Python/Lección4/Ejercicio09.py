# Ejercicio 9: Mostrar una frace sin espacios y contar su longitud
# Hacer un programa donde el usuario ingrese una frase, se le
# devolcerá la misma frase pero sin espacios en blanco, y
# además un contador de cuántos caracteres tiene la frase
# (sin contar los espacios en blanco)
# Ejemplo:          frase = vivir por siempre en paz
#                   frase = vivirporsiempreenpaz
#                   N° de caracteres = 21

frase1 = input("Ingresar una frase: ")
frase2 = " "
for i in frase1:
    if i != " ":
        frase2 += i
frase1 = frase2
print(f"\n Frase final: {frase1}")
print(f"N° de caracteres: {len(frase1)}")
