class Figuras:
    # Metodo constructor
    def __init__(self, nombre, lados, vertices):
        # Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.lados = lados
        self.vertices = vertices

    # Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información de la Figura")    
        print("Nombre: " + self.nombre)
        print("Lados: " + self.lados)
        print("Vértices: " + self.vertices)
        print("-------------------------------------------")

    # Método para calcular el área 
    def calcular_area(self):
        self.opcion = input("¿De qué figura desea calcular el área? (TRIANGULO/PENTAGONO/RECTANGULO): ")
        if self.nombre == "TRIANGULO":
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            return 0.5 * base * altura
        elif self.nombre == "PENTAGONO":
            lado = float(input("Ingrese el lado del pentágono: "))
            apotema = float(input("Ingrese el apotema del pentágono: "))
            perimetro = 5 * lado
            return 0.5 * perimetro * apotema
        elif self.nombre == "RECTANGULO":
            largo = float(input("Ingrese el largo del rectángulo: "))
            ancho = float(input("Ingrese el ancho del rectángulo: "))
            return largo * ancho
        else:
            return "Figura no soportada para el cálculo de área."

# Creamos los objetos
figura1 = Figuras("TRIANGULO", "3", "3")
figura2 = Figuras("PENTAGONO", "5", "5")
figura3 = Figuras("RECTANGULO", "4", "4")

# Mostrar los detalles de cada objeto
figura1.mostrar_detalles()
figura2.mostrar_detalles()
figura3.mostrar_detalles()
figura1.calcular_area()


