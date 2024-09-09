def nba_extrap(ppg, mpg):
    """
    Esta función extrapola los puntos por juego (ppg) de un jugador de baloncesto a si jugara un partido completo de 48 minutos.
    Argumentos:
    ppg (float/int): Puntos por juego que anota el jugador.
    mpg (float/int): Minutos por juego que juega el jugador.
    Retorna:
    float: Los puntos extrapolados si el jugador jugara los 48 minutos, redondeados a la décima más cercana.
    Si el jugador no ha jugado ningún minuto (mpg == 0), retorna 0.
    """
    # Si el jugador no ha jugado ningún minuto, retorna 0
    if mpg == 0:
        return 0
    # Extrapolación de puntos por 48 minutos
    ppg_48 = (ppg * 48) / mpg
    # Redondeo a la décima más cercana
    return round(ppg_48, 1)

# Ejemplos de uso
print("ejemplo de uso estatico")
print(nba_extrap(12, 20))  # Salida esperada: 28.8
print(nba_extrap(10, 10))  # Salida esperada: 48.0
print(nba_extrap(5, 17))  # Salida esperada: 14.1
print(nba_extrap(0, 0))  # Salida esperada: 0
print("ejemplo de uso dinamico")
ppg = float(input("Ingresa los puntos por juego (ppg): "))
mpg = float(input("Ingresa los minutos por juego (mpg): "))

# Llamar a la función con los valores ingresados
resultado = nba_extrap(ppg, mpg)

# Mostrar el resultado
print(f"Si el jugador jugara 48 minutos, anotaría aproximadamente {resultado} puntos.")