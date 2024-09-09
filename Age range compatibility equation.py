import math

def dating_range(age):
    """
    Esta función calcula el rango de edad mínimo y máximo compatible para una persona.
    Argumentos:
    age (int): La edad de la persona para la que se va a calcular el rango.
    Retorna:
    str: El rango de edad mínimo y máximo en formato '[min]-[max]'.
    """
    if age > 14:
        # Fórmula para personas mayores de 14 años
        min_age = math.floor((age / 2) + 7)
        max_age = math.floor((age - 7) * 2)
    else:
        # Fórmula para personas de 14 años o menos
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)
    return f"{min_age}-{max_age}"

# Entrada del usuario
age = int(input("Ingresa la edad: "))
# Resultado
print(f"El rango de edad compatible es: {dating_range(age)}")
