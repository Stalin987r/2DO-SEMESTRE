# --------------------------------------------
# PROGRAMA: Promedio semanal del clima
# PARADIGMA: Programación Orientada a Objetos
# --------------------------------------------

class Clima:
    """
    Clase que representa el registro del clima semanal.
    Aplica encapsulamiento usando atributos privados.
    """

    def __init__(self):
        self.__temperaturas = []  # Atributo privado (encapsulamiento)

    def ingresar_temperaturas(self):
        """
        Método para ingresar las temperaturas diarias
        """
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

        for dia in dias:
            temp = float(input(f"Ingrese la temperatura del {dia}: "))
            self.__temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Método para calcular el promedio semanal
        """
        return sum(self.__temperaturas) / len(self.__temperaturas)


# Clase hija (ejemplo de herencia)
class ClimaExtendido(Clima):
    """
    Clase que hereda de Clima y extiende su funcionalidad
    """

    def mostrar_resultado(self):
        promedio = self.calcular_promedio()
        print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")


# Programa principal
print("=== Promedio Semanal del Clima (POO) ===")
clima = ClimaExtendido()
clima.ingresar_temperaturas()
clima.mostrar_resultado()
