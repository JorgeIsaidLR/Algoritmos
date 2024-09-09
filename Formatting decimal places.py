
def round_to_two_decimals(number):
    """
    Función para redondear un número a dos decimales.
    Parámetros:
    number (float): El número que se desea redondear.
    Retorna:
    float: El número redondeado a dos decimales.
    Ejemplo:
    >>> round_to_two_decimals(5.5589)
    5.56
    >>> round_to_two_decimals(3.3424)
    3.34
    """
    return round(number, 2)
def main():
    """
    Función principal que solicita al usuario ingresar números,
    los redondea a dos decimales y los imprime.
    El usuario puede ingresar múltiples números separados por comas.
    Ejemplo:
    Entrada: 5.5589, 3.3424
    Salida: 5.56, 3.34
    """
    # Solicitar entrada del usuario y convertirla en una lista de números flotantes
    user_input = input("Ingrese números separados por comas: ")
    numbers = [float(num) for num in user_input.split(",")]

    # Redondear cada número a dos decimales
    rounded_numbers = [round_to_two_decimals(num) for num in numbers]

    # Mostrar los resultados redondeados
    print("Números redondeados a dos decimales:", rounded_numbers)


if __name__ == "__main__":
    main()
