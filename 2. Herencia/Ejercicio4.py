class Instrumento:
    # Constructor
    def __init__(self, tipo, marca, material_fabricacion, precio):
        self.tipo = tipo
        self.marca = marca
        self.material_fabricacion = material_fabricacion
        self.precio = precio
        self.tamano = float(input("Ingrese el tamaño del instrumento en cm: "))

    # Métodos públicos
    def registrar(self):
        print("--------------------")
        print("INSTRUMENTO REGISTRADO")
        print("--------------------")
        print("Tipo: ", self.tipo)
        print("Marca: ", self.marca)
        print("Material de fabricación: ", self.material_fabricacion)
        print("Precio: ", self.precio)
        print("Tamaño: ", self.tamano, "cm")

class Guitarra(Instrumento):  # Subclase Guitarra
    # Constructor
    def __init__(self, tipo, marca, material_fabricacion, precio, numero_cuerdas):
        super().__init__(tipo, marca, material_fabricacion, precio)  # Llamada al constructor de la superclase
        self.numero_cuerdas = numero_cuerdas

    # Método privado
    def detalles_cuerdas(self):
        print("--------------------")
        print(f"La guitarra {self.marca} tiene {self.numero_cuerdas} cuerdas")

# Instanciando la subclase Guitarra
objeto_guitarra = Guitarra('Eléctrica', 'Fender', 'Madera', 599, 6)
objeto_guitarra.registrar()
objeto_guitarra.detalles_cuerdas()
