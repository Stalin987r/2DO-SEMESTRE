# --------------------------------------------
# PROGRAMA: Promedio semanal del clima
# PARADIGMA: Programación Tradicional
# --------------------------------------------

# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    for dia in dias:
        temp = float(input(f"Ingrese la temperatura del {dia}: "))
        temperaturas.append(temp)

    return temperaturas


# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio


# Función principal
def main():
    print("=== Promedio Semanal del Clima (Programación Tradicional) ===")
    temperaturas = ingresar_temperaturas()
    promedio_semanal = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperatura es: {promedio_semanal:.2f} °C")


# Ejecución del programa
main()
