"""
PROGRAMA QUE CALCULA LA EDAD DE UN PERRO Y UN GATO EN AÑOS HUMANOS
"""
#calcula la edad del perro y el gato en años hunamnosf
def calcular_edad_animal(humanYears):
    # Años de gato
    if humanYears == 1:
        catYears = 15
    elif humanYears == 2:
        catYears = 15 + 9
    else:
        catYears = 15 + 9 + (humanYears - 2) * 4
    # Años de perro
    if humanYears == 1:
        dogYears = 15
    elif humanYears == 2:
        dogYears = 15 + 9
    else:
        dogYears = 15 + 9 + (humanYears - 2) * 5

    return [humanYears, catYears, dogYears]

huma_years = int(input("DAME LOS AÑOS HUMANOS: *"))
# Ejemplo de uso
resultado = calcular_edad_animal(huma_years)
#  Imprime el tipo de datos devuelto por la función
print(resultado)  # Output: [3, 28, 29]

# input()

print(f"los años en humanos son: {resultado[0]}*" )
print(f"Los años del gato son: {resultado[1]}*" )
print(f"Los años del gato son: {resultado[2]}*" )


