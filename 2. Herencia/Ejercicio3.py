class Electronico:
    # Constructor
    def __init__(self, marca, modelo, precio, color):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.color = color

    # Método para mostrar la información básica
    def mostrar_informacion(self):
        print("--------------------")
        print("INFORMACIÓN DEL ELECTRÓNICO")
        print("--------------------")
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Precio: ", self.precio)
        print("Color: ", self.color)

class Laptop(Electronico):
    # Constructor
    def __init__(self, marca, modelo, precio, color, tamanio_pantalla, capacidad_bateria):
        super().__init__(marca, modelo, precio, color)
        self.tamanio_pantalla = tamanio_pantalla
        self.capacidad_bateria = capacidad_bateria

    # Método para mostrar la información específica de la laptop
    def mostrar_informacion_laptop(self):
        self.mostrar_informacion()  
        print("Tamaño de Pantalla: ", self.tamanio_pantalla, "pulgadas")
        print("Capacidad de Batería: ", self.capacidad_bateria, "mAh")

# Instanciando la clase Laptop
laptop = Laptop('Dell', 'XPS 13', 1200, 'Plata', 13.3, 5000)
laptop.mostrar_informacion_laptop()
