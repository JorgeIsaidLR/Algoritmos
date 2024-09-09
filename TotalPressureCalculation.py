"""
PROGRAMA PARA CALCULAR LA PRESION TOTAL APLICADA
"""
def calcular_presion_total(m1, M1, m2, M2, V, T):
    # Constante de gases ideales
    R = 0.082  # dm^3 * atm / (K * mol)

    # Convertir temperatura de °C a Kelvin
    T_kelvin = T + 273.15
    # Cálculo del número de moles de cada gas
    n1 = m1 / M1  # moles de gas 1
    n2 = m2 / M2  # moles de gas 2

    # Suma total de moles
    n_total = n1 + n2
    # Aplicar la fórmula para calcular la presión total
    P_total = (n_total * R * T_kelvin) / V
    return P_total

# Ejemplo de uso
m1 = float(input("Introduce la masa del gas 1 (g): "))
M1 = float(input("Introduce la masa molar del gas 1 (g/mol): "))
m2 = float(input("Introduce la masa del gas 2 (g): "))
M2 = float(input("Introduce la masa molar del gas 2 (g/mol): "))
V = float(input("Introduce el volumen del recipiente (dm^3): "))
T = float(input("Introduce la temperatura (°C): "))

# Calcular la presión total
presion_total = calcular_presion_total(m1, M1, m2, M2, V, T)
print(f"La presión total es: {presion_total:.2f} atm")
