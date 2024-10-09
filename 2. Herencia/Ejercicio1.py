class Dispositivo:
    # Constructor
    def __init__(self, marca, modelo, precio, color):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.color = color
        self.almacenamiento = int(input("Ingrese el almacenamiento en GB: "))

    # Métodos públicos
    def registrar(self):
        print("--------------------")
        print("DISPOSITIVO REGISTRADO")
        print("--------------------")
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Precio: ", self.precio)
        print("Color: ", self.color)
        print("Almacenamiento: ", self.almacenamiento, "GB")

class Smartphone(Dispositivo):  # Subclase Smartphone
    # Constructor
    def __init__(self, marca, modelo, precio, color, sistema_operativo):
        super().__init__(marca, modelo, precio, color)  # Llamada al constructor de la superclase
        self.sistema_operativo = sistema_operativo
        self.camara_megapixeles = int(input("Ingrese la cámara en megapíxeles: "))

    # Método privado
    def detalles_camara(self):
        print("Sistema Operativo: ", self.sistema_operativo)
        if self.camara_megapixeles >= 12:
            print("--------------------")
            print(f"El dispositivo {self.modelo} tiene una cámara de alta calidad")
        else:
            print("--------------------")
            print(f"El dispositivo {self.modelo} tiene una cámara estándar")

# Instanciando la subclase Smartphone
objeto_smartphone = Smartphone('Samsung', 'Galaxy S23', 799, 'Negro', 'Android')
objeto_smartphone.registrar()
objeto_smartphone.detalles_camara()
