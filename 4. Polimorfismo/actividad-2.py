# Clase padre Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")

# Clase hija Carro
class Carro(Vehiculo):
    def __init__(self, marca, modelo, color, puertas):
        super().__init__(marca, modelo, color)
        self.puertas = puertas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Puertas: {self.puertas}")

# Clase hija Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, color, cilindrada):
        super().__init__(marca, modelo, color)
        self.cilindrada = cilindrada

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cilindrada: {self.cilindrada} cc")

# Clase hija Bicicleta
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, color, tipo):
        super().__init__(marca, modelo, color)
        self.tipo = tipo

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de bicicleta: {self.tipo}")

# Función que muestra la información de cualquier tipo de vehículo
def mostrar_informacion(vehiculo):
    vehiculo.mostrar_info()

# Instancias de cada clase
objeto_carro = Carro("Toyota", "Corolla", "Rojo", 4)
objeto_moto = Moto("Yamaha", "R15", "Azul", 150)
objeto_bicicleta = Bicicleta("Giant", "Talon", "Negro", "Montaña")

# Llamado al método mostrar_info para cada objeto
mostrar_informacion(objeto_carro)
mostrar_informacion(objeto_moto)
mostrar_informacion(objeto_bicicleta)
