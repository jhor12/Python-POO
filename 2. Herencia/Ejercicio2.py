class Electrodomestico:
    # constructor
    def __init__(self, marca, color, capacidad):
        self.marca = marca
        self.color = color
        self.capacidad = capacidad
        self.consumo_electrico = int(input("Digite el consumo electrico en kw: "))

    # métodos públicos
    def registrar(self):
        print("--------------------")
        print("ELECTRODOMÉSTICO REGISTRADO")
        print("--------------------")
        print("Marca: ", self.marca)
        print("Color: ", self.color)
        print("Capacidad: ", self.capacidad)
        print("Consumo eléctrico: ", self.consumo_electrico)


class Refrigerador(Electrodomestico):  # subclase Refrigerador
    # constructor
    def __init__(self, marca, color, capacidad, tiporefrigerador):
        super().__init__(marca, color, capacidad)  # llamada al constructor de la superclase
        self.tiporefrigerador = tiporefrigerador
        self.temperatura = int(input("Ingrese la temperatura: "))

    # método privado
    def ajustar(self):
        print("Tipo de refrigerador: ", self.tiporefrigerador)

        if self.temperatura > 10:
            print("--------------------")
            print(f"El electrodoméstico de color {self.color} con capacidad {self.capacidad} tiene una temperatura estable!!")
        else:
            print("--------------------")
            print(f"El electrodoméstico de color {self.color} no enciende!!")


# instanciando la subclase Refrigerador
objeto_refrigerador = Refrigerador('HACEB', 'GRIS', '2000LT', 'FROST')
objeto_refrigerador.registrar()
objeto_refrigerador.ajustar()
