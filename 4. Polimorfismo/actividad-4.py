# Clase padre Instrumentos Musicales
class InstrumentosMusicales:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def mostrar_info(self):
        print(f"Instrumento: {self.nombre}")
        print(f"Tipo: {self.tipo}")

    def tocar(self):
        pass  # Método que será sobrescrito por las clases hijas

# Clase hija Guitarra
class Guitarra(InstrumentosMusicales):
    def __init__(self, nombre, tipo, cuerdas):
        super().__init__(nombre, tipo)
        self.cuerdas = cuerdas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cuerdas: {self.cuerdas}")

    def tocar(self):
        print(f"{self.nombre} suena: ¡Trum Trum!")

# Clase hija Piano
class Piano(InstrumentosMusicales):
    def __init__(self, nombre, tipo, teclas):
        super().__init__(nombre, tipo)
        self.teclas = teclas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Teclas: {self.teclas}")

    def tocar(self):
        print(f"{self.nombre} suena: ¡Plin plon!")

# Clase hija Trompeta
class Trompeta(InstrumentosMusicales):
    def __init__(self, nombre, tipo, material):
        super().__init__(nombre, tipo)
        self.material = material

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Material: {self.material}")

    def tocar(self):
        print(f"{self.nombre} suena: ¡Tuau tau!")

# Función que muestra la información y sonido de cualquier tipo de instrumento
def mostrar_informacion(instrumento):
    instrumento.mostrar_info()
    instrumento.tocar()

# Instancias de cada clase
objeto_guitarra = Guitarra("Guitarra Acústica", "Cuerda", 6)
objeto_piano = Piano("Piano de Cola", "Teclado", 88)
objeto_trompeta = Trompeta("Trompeta Bb", "Viento", "Latón")

# Llamado al método mostrar_info y tocar para cada objeto
mostrar_informacion(objeto_guitarra)
mostrar_informacion(objeto_piano)
mostrar_informacion(objeto_trompeta)
