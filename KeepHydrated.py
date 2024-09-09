import math
def calcular_litros(time):
    """
    Calcula la cantidad de litros de agua que Nathan beberá durante su sesión de ciclismo.
    Argumentos:
    time -- Tiempo en horas (puede ser decimal).
    Retorna:
    El número entero de litros de agua, redondeado hacia abajo.
    """
    # Cantidad de agua que Nathan bebe por hora de ciclismo
    litros_por_hora = 0.5

    # Calcular los litros de agua totales
    litros = time * litros_por_hora

    # Redondear hacia abajo para obtener un valor entero
    return math.floor(litros)


# Ejemplo de uso:
# time = 3
time = int(input("ingresa las horas que practicaras ciclismo:"))
print(f"Litros para {time} horas: {calcular_litros(time)}")  # Output: 1
print("Ejemplo estatico=")
time = 6.7
print(f"Litros para {time} horas: {calcular_litros(time)}")  # Output: 3

time = 11.8
print(f"Litros para {time} horas: {calcular_litros(time)}")  # Output: 5
