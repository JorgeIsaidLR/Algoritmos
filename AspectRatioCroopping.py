# programa que renderiza los pixeles para las nuevas medidas de
# las imagenes

import math # Importamos el módulo math para usar la función ceil, que redondea hacia arriba.
"""
    Ajusta la resolución de una imagen a un aspecto de 16:9, manteniendo la altura (y) y recalculando el ancho (x).

    Argumentos:
    x -- Ancho actual de la imagen en píxeles.
    y -- Altura actual de la imagen en píxeles.

    Retorna:
    Una tupla (nuevo_ancho, nueva_altura) con el nuevo ancho ajustado para una relación de 16:9,
    y la altura original, redondeando el ancho al entero superior más cercano.
"""


def ajustar_a_16_9(x, y):
    # Calculamos el nuevo ancho para que la relación sea 16:9, manteniendo la altura (y)
    nuevo_ancho = math.ceil((16 / 9) * y)

    # Retornamos las nuevas resoluciones ajustadas
    return nuevo_ancho, y


# Ejemplo de uso
# x, y = 374, 280
# resultado 498 * 280

x = int(input("Ingrese el valor de x "))
y = int(input("Ingrese el valor de y "))

nuevo_x, nuevo_y = ajustar_a_16_9(x, y)
print(f"Nueva resolución: {nuevo_x} × {nuevo_y}")
