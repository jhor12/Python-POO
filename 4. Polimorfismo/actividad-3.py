# Clase padre Animales
class Animales:
    def __init__(self, nombre, edad, color):
        self.nombre = nombre
        self.edad = edad
        self.color = color

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Color: {self.color}")

    def sonido(self):
        pass  # Método que será sobreescrito por las clases hijas

# Clase hija Perro
class Perro(Animales):
    def __init__(self, nombre, edad, color, raza):
        super().__init__(nombre, edad, color)
        self.raza = raza

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Raza: {self.raza}")

    def sonido(self):
        print(f"{self.nombre} dice: ¡Guau Guau!")

# Clase hija Gato
class Gato(Animales):
    def __init__(self, nombre, edad, color, pelaje):
        super().__init__(nombre, edad, color)
        self.pelaje = pelaje

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de pelaje: {self.pelaje}")

    def sonido(self):
        print(f"{self.nombre} dice: ¡Miau Miau!")

# Clase hija Pájaro
class Pajaro(Animales):
    def __init__(self, nombre, edad, color, especie):
        super().__init__(nombre, edad, color)
        self.especie = especie

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Especie: {self.especie}")

    def sonido(self):
        print(f"{self.nombre} dice: ¡Pío Pío!")

# Función que muestra la información y sonido de cualquier tipo de animal
def mostrar_informacion(animal):
    animal.mostrar_info()
    animal.sonido()

# Instancias de cada clase
objeto_perro = Perro("Rex", 5, "Marrón", "Labrador")
objeto_gato = Gato("Mixter", 3, "Blanco", "Corto")
objeto_pajaro = Pajaro("Mateo", 2, "Amarillo", "Canario")

# Llamado al método mostrar_info y sonido para cada objeto
mostrar_informacion(objeto_perro)
mostrar_informacion(objeto_gato)
mostrar_informacion(objeto_pajaro)
