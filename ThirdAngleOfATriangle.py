def tercer_angulo(angulo1, angulo2):
    """
    Calcula el tercer ángulo de un triángulo dado que se conocen los otros dos ángulos interiores.
    Argumentos:
    angulo1 -- Primer ángulo interior del triángulo (en grados, entero positivo).
    angulo2 -- Segundo ángulo interior del triángulo (en grados, entero positivo).
    Retorna:
    El valor del tercer ángulo (en grados, entero positivo).
    """
    # La suma de los ángulos interiores de un triángulo es siempre 180 grados
    tercer_angulo = 180 - (angulo1 + angulo2)

    # Retornamos el valor del tercer ángulo
    return tercer_angulo

# Ejemplo de uso:
#angulo1 = 60  # Primer ángulo interior
#angulo2 = 60  # Segundo ángulo interior
# Resultado 60 grados
##
angulo1 = int(input("Favor de introducir el angulo 1:"))
angulo2 = int(input("Favor de introducir el angulo 2:"))

resultado = tercer_angulo(angulo1, angulo2)
print(f"El tercer ángulo es: {resultado} grados")  # Output: El tercer ángulo es: 60 grados

# angulo1 = 45
# angulo2 = 90
# Resultado = 45
angulo1 = int(input("Favor de introducir el angulo 1:"))
angulo2 = int(input("Favor de introducir el angulo 2:"))
resultado = tercer_angulo(angulo1, angulo2)
print(f"El tercer ángulo es: {resultado} grados")  # Output: El tercer ángulo es: 45 grados
