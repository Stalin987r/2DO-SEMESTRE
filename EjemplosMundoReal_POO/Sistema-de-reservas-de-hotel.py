# Clase Habitacion
# Representa una habitación del hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero      # Número de la habitación
        self.tipo = tipo          # Tipo de habitación (Simple, Doble, Suite)
        self.precio = precio      # Precio por noche
        self.disponible = True    # Estado de disponibilidad

    # Método para reservar la habitación
    def reservar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    # Método para liberar la habitación
    def liberar(self):
        self.disponible = True


# Clase Cliente
# Representa a un cliente del hotel
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula


# Clase Reserva
# Representa una reserva realizada por un cliente
class Reserva:
    def __init__(self, cliente, habitacion, noches):
        self.cliente = cliente
        self.habitacion = habitacion
        self.noches = noches

    # Método para calcular el costo total de la reserva
    def calcular_total(self):
        return self.habitacion.precio * self.noches


# Clase Hotel
# Administra las habitaciones y reservas
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []   # Lista de habitaciones
        self.reservas = []       # Lista de reservas

    # Agregar una habitación al hotel
    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    # Mostrar habitaciones disponibles
    def mostrar_disponibles(self):
        for h in self.habitaciones:
            if h.disponible:
                print(f"Habitación {h.numero} - {h.tipo} - ${h.precio}")

    # Realizar una reserva
    def realizar_reserva(self, cliente, numero_habitacion, noches):
        for h in self.habitaciones:
            if h.numero == numero_habitacion and h.disponible:
                h.reservar()
                reserva = Reserva(cliente, h, noches)
                self.reservas.append(reserva)
                print(f"Reserva realizada para {cliente.nombre}")
                print(f"Total a pagar: ${reserva.calcular_total()}")
                return
        print("Habitación no disponible o no existe")


# ==========================
# PROGRAMA PRINCIPAL
# ==========================

# Crear el hotel
hotel = Hotel("Hotel Paraíso")

# Crear habitaciones
habitacion1 = Habitacion(101, "Simple", 30)
habitacion2 = Habitacion(102, "Doble", 50)
habitacion3 = Habitacion(103, "Suite", 80)

# Agregar habitaciones al hotel
hotel.agregar_habitacion(habitacion1)
hotel.agregar_habitacion(habitacion2)
hotel.agregar_habitacion(habitacion3)

# Crear un cliente
cliente1 = Cliente("Juan Pérez", "0102030405")

# Mostrar habitaciones disponibles
print("Habitaciones disponibles:")
hotel.mostrar_disponibles()

# Realizar una reserva
hotel.realizar_reserva(cliente1, 102, 3)
