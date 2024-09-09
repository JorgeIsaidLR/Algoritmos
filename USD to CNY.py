def convertir_usd_a_cny(usd):
    """
    Convierte una cantidad de dólares estadounidenses (USD) a yuanes chinos (CNY).
    Argumentos:
    usd -- Cantidad de dólares en formato entero.
    Retorna:
    Una cadena que representa la cantidad equivalente en yuanes chinos (CNY),
    seguida del texto 'Chinese Yuan'. El valor se muestra con dos decimales.
    """
    # Tasa de conversión de USD a CNY
    tasa_conversion = 6.75

    # Calcular el equivalente en yuanes chinos
    cny = usd * tasa_conversion

    # Retornar la cantidad en yuanes como cadena con dos decimales
    return f"{cny:.2f} Chinese Yuan"


# Ejemplo de uso:
# usd = 15  # Cantidad en USD
usd = int(input("Favor de insertar los dolares a convertir: "))
resultado = convertir_usd_a_cny(usd)
print(resultado)  # Output: '101.25 Chinese Yuan'
usd = int(input("Favor de insertar una cantidad mayor para convertir:"))
#usd = 465  # Otro ejemplo con mayor cantidad
resultado = convertir_usd_a_cny(usd)
print(resultado)  # Output: '3138.75 Chinese Yuan'
