# Se utiliza tuplas para definir los tipos de vehículos permitidos y sus tarifas correspondientes. Se implementa una clase Parqueadero que maneja el ingreso y salida de vehículos, así como el cálculo de cobros y la generación de reportes.

TIPOS_PERMITIDOS = ("carro", "moto", "bicicleta")

#Diccionario que guarda el precio por hora de cada vehiculo
TARIFAS = {
    "carro": 3000,
    "moto": 1500,
    "bicicleta": 500
}

# Funcion para calcular cuanto debe pagar cada vehiculo
def calcular_cobro(tipo, horas, descuento=0):
    if horas < 1:
        horas = 1

    total = TARIFAS[tipo] * horas
    valor_descuento = total * descuento / 100
    total = total - valor_descuento
    return total

#Funcion para verificar la placa de los vehiculos ingresados, si la placa tiene 6 caracteres retorna True, de lo contrario retorna False

def placa_valida(placa):
    if len(placa) == 6:
        return True
    else:
        return False

# Agrupa los datos y las acciones del parqueadero
class Parqueadero:

    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.vehiculos = []
        self.historial = []

# registra el ingreso del vehiculo F O V
    def ingresar(self, placa, tipo, conductor):
        if len(self.vehiculos) >= self.capacidad:
            print("Ingreso rechazado: el parqueadero está lleno")
            return False

        if tipo not in TIPOS_PERMITIDOS:
            print("Ingreso rechazado: tipo de vehículo no permitido")
            return False

        if not placa_valida(placa):
            print("Ingreso rechazado: la placa debe tener 6 caracteres")
            return False

        for vehiculo in self.vehiculos:
            if vehiculo["placa"] == placa:
                print("Ingreso rechazado: el vehículo ya está adentro")
                return False

        nuevo = {"placa": placa, "tipo": tipo, "conductor": conductor}
        self.vehiculos.append(nuevo)
        print("Vehículo", placa, "ingresó correctamente")
        return True

# registra la salida del vehiculo y calcula el cobro correspondiente
    def salir(self, placa, horas, descuento=0):
        for vehiculo in self.vehiculos:
            if vehiculo["placa"] == placa:
                valor = calcular_cobro(vehiculo["tipo"], horas, descuento)

                registro = (placa, vehiculo["tipo"], horas, valor)
                self.historial.append(registro)

                self.vehiculos.remove(vehiculo)

                print("Vehículo", placa, "salió. Total a pagar:", valor)
                return valor

        print("No se encontró un vehículo con la placa", placa)
        return None

# placas ya ingresadas al parqueadero 
    def placas_dentro(self):
        placas = []
        for vehiculo in self.vehiculos:
            placas.append(vehiculo["placa"])
        return placas

# suma el el dinero recaudado por todos los vehiculos que han salido del parqueadero

    def total_recaudado(self):
        total = 0
        for registro in self.historial:
            total = total + registro[3]
        return total

#  se utiliza diccionario con el dinero recaudado por cada tipo de vehiculo que ha salido del parqueadero

    def reporte_por_tipo(self):
        reporte = {}

        for tipo in TIPOS_PERMITIDOS:
            reporte[tipo] = 0

        for registro in self.historial:
            tipo = registro[1]
            valor = registro[3]
            reporte[tipo] = reporte[tipo] + valor

        return reporte

# parqueadero con capacidad para tres vehiculos 
mi_parqueadero = Parqueadero(3)

print("--- Ingresos ---")
mi_parqueadero.ingresar("ABC123", "carro", "Gabriel")
mi_parqueadero.ingresar("XYZ789", "moto", "Leanny")
mi_parqueadero.ingresar("BIC001", "bicicleta", "Carlos")
mi_parqueadero.ingresar("ABC123", "carro", "Juliana")
mi_parqueadero.ingresar("AAA111", "carro", "Luis")
mi_parqueadero.ingresar("AB12", "moto", "Nikol")
mi_parqueadero.ingresar("CAM123", "camion", "Eduardo")

print("--- Placas adentro ---")
print(mi_parqueadero.placas_dentro())

print("--- Salidas ---")
mi_parqueadero.salir("ABC123", 2)
mi_parqueadero.salir("XYZ789", 0.5)
mi_parqueadero.salir("BIC001", 3, 10)

print("--- Placas adentro ---")
print(mi_parqueadero.placas_dentro())

print("--- Total recaudado ---")
print(mi_parqueadero.total_recaudado())

print("--- Reporte por tipo ---")
print(mi_parqueadero.reporte_por_tipo())