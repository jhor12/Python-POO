class Reloj:
    # Constructor
    def __init__(self, marca, modelo, precio, color):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.color = color

    # Método para mostrar la información básica del reloj
    def mostrar_informacion(self):
        print("--------------------")
        print("INFORMACIÓN DEL RELOJ")
        print("--------------------")
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Precio: ", self.precio)
        print("Color: ", self.color)

class RelojInteligente(Reloj):
    # Constructor
    def __init__(self, marca, modelo, precio, color, sistema_operativo, duracion_bateria):
        super().__init__(marca, modelo, precio, color)
        self.sistema_operativo = sistema_operativo
        self.duracion_bateria = duracion_bateria

    # Método para mostrar la información específica del reloj inteligente
    def mostrar_informacion_reloj_inteligente(self):
        self.mostrar_informacion()  
        print("Sistema Operativo: ", self.sistema_operativo)
        print("Duración de la Batería: ", self.duracion_bateria, "horas")

# Instanciando la clase RelojInteligente
reloj_inteligente = RelojInteligente('Apple', 'Watch Series 8', 399, 'Negro', 'watchOS', 18)
reloj_inteligente.mostrar_informacion_reloj_inteligente()
