# ACTIVIDAD EXTRA - PARQUEADERO DEL CENTRO COMERCIAL

# 1. Tupla con los tipos de vehículo permitidos
TIPOS_PERMITIDOS = ("carro", "moto", "bicicleta")

# 2. Diccionario con el valor por hora de cada tipo
TARIFAS = {
    "carro": 3000,
    "moto": 1500,
    "bicicleta": 500
}


# 3. Función que calcula el cobro
# El descuento se recibe como porcentaje (ejemplo: 10 significa 10%)
def calcular_cobro(tipo, horas, descuento=0):
    # Si estuvo menos de 1 hora, se cobra 1 hora completa
    if horas < 1:
        horas = 1

    total = TARIFAS[tipo] * horas
    valor_descuento = total * descuento / 100
    total = total - valor_descuento
    return total


# 4. Función que revisa si la placa tiene exactamente 6 caracteres
def placa_valida(placa):
    if len(placa) == 6:
        return True
    else:
        return False


# 5. Clase Parqueadero
class Parqueadero:

    def __init__(self, capacidad):
        self.capacidad = capacidad   # número máximo de vehículos
        self.vehiculos = []          # lista de diccionarios: {"placa", "tipo", "conductor"}
        self.historial = []          # lista de tuplas: (placa, tipo, horas, valor_pagado)

    # 6. Método para ingresar un vehículo
    def ingresar(self, placa, tipo, conductor):
        # Si el parqueadero está lleno
        if len(self.vehiculos) >= self.capacidad:
            print("Ingreso rechazado: el parqueadero está lleno")
            return False

        # Si el tipo no está permitido
        if tipo not in TIPOS_PERMITIDOS:
            print("Ingreso rechazado: tipo de vehículo no permitido")
            return False

        # Si la placa no es válida
        if not placa_valida(placa):
            print("Ingreso rechazado: la placa debe tener 6 caracteres")
            return False

        # Si el vehículo ya está adentro
        for vehiculo in self.vehiculos:
            if vehiculo["placa"] == placa:
                print("Ingreso rechazado: el vehículo ya está adentro")
                return False

        # Si pasó todas las validaciones, entra
        nuevo = {"placa": placa, "tipo": tipo, "conductor": conductor}
        self.vehiculos.append(nuevo)
        print("Vehículo", placa, "ingresó correctamente")
        return True

    # 7. Método para sacar un vehículo
    def salir(self, placa, horas, descuento=0):
        # Buscamos el vehículo en la lista
        for vehiculo in self.vehiculos:
            if vehiculo["placa"] == placa:
                valor = calcular_cobro(vehiculo["tipo"], horas, descuento)

                # Guardamos en el historial
                registro = (placa, vehiculo["tipo"], horas, valor)
                self.historial.append(registro)

                # Lo sacamos de los vehículos que están adentro
                self.vehiculos.remove(vehiculo)

                print("Vehículo", placa, "salió. Total a pagar:", valor)
                return valor

        print("No se encontró un vehículo con la placa", placa)
        return None

    # 8. Método que devuelve las placas de los vehículos que están adentro
    def placas_dentro(self):
        placas = []
        for vehiculo in self.vehiculos:
            placas.append(vehiculo["placa"])
        return placas

    # 9. Método que suma los pagos del historial
    def total_recaudado(self):
        total = 0
        for registro in self.historial:
            total = total + registro[3]   # posición 3 = valor_pagado
        return total

    # 10. Método que devuelve cuánto se recaudó por cada tipo
    def reporte_por_tipo(self):
        reporte = {}

        # Empezamos todos los tipos en 0
        for tipo in TIPOS_PERMITIDOS:
            reporte[tipo] = 0

        # Sumamos cada pago al tipo que le corresponde
        for registro in self.historial:
            tipo = registro[1]      # posición 1 = tipo
            valor = registro[3]     # posición 3 = valor_pagado
            reporte[tipo] = reporte[tipo] + valor

        return reporte


# ---------------- PRUEBAS DEL PROGRAMA ----------------
mi_parqueadero = Parqueadero(3)

print("--- Ingresos ---")
mi_parqueadero.ingresar("ABC123", "carro", "Juan")
mi_parqueadero.ingresar("XYZ789", "moto", "Maria")
mi_parqueadero.ingresar("BIC001", "bicicleta", "Pedro")
mi_parqueadero.ingresar("ABC123", "carro", "Juan")    # ya está adentro
mi_parqueadero.ingresar("AAA111", "carro", "Luis")    # parqueadero lleno
mi_parqueadero.ingresar("AB12", "moto", "Ana")        # placa no válida
mi_parqueadero.ingresar("CAM123", "camion", "Raul")   # tipo no permitido

print("--- Placas adentro ---")
print(mi_parqueadero.placas_dentro())

print("--- Salidas ---")
mi_parqueadero.salir("ABC123", 2)        # 2 horas de carro = 6000
mi_parqueadero.salir("XYZ789", 0.5)      # menos de 1 hora, se cobra 1 = 1500
mi_parqueadero.salir("BIC001", 3, 10)    # 3 horas con 10% de descuento = 1350

print("--- Placas adentro ---")
print(mi_parqueadero.placas_dentro())

print("--- Total recaudado ---")
print(mi_parqueadero.total_recaudado())

print("--- Reporte por tipo ---")
print(mi_parqueadero.reporte_por_tipo())