def mango(cantidad, precio_por_mango):
    """
    Calcula el costo total de los mangos considerando la oferta "3 por 2".
    Argumentos:
    cantidad -- La cantidad total de mangos.
    precio_por_mango -- El precio de cada mango.
    Retorna:
    El costo total, considerando la oferta de que por cada 3 mangos, solo pagas por 2.
    """

    # Calcular la cantidad de mangos que se pagan (2 de cada 3)
    mangos_que_se_pagan = (cantidad // 3) * 2 + (cantidad % 3)

    # Calcular el costo total
    costo_total = mangos_que_se_pagan * precio_por_mango

    return costo_total


# Ejemplo de uso estatico:
print(mango(2, 3))  # Output: 6
print(mango(3, 3))  # Output: 6
print(mango(5, 3))  # Output: 12
print(mango(9, 5))  # Output: 30

# Solicitar la cantidad de mangos y el precio por mango al usuario
cantidad = int(input("Ingresa la cantidad de mangos: "))
precio = float(input("Ingresa el precio por cada mango: "))

# Llamar a la función mango con los valores ingresados por el usuario
total = mango(cantidad, precio)

# Mostrar el costo total
print(f"El costo total es: {total}")