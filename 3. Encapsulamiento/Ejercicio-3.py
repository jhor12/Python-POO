# Clase Libros con atributos encapsulados o privados
class Libros:
    # Método constructor
    def __init__(self, titulo, autor, isbn, portada):
        self.__titulo = titulo  # privado
        self.__autor = autor  # privado
        self.__isbn = isbn  # privado
        self.portada = portada  # público

    # Método getter
    def obtener_titulo(self):
        return self.__titulo

    # Método getter
    def obtener_autor(self):
        return self.__autor

    # Método getter
    def obtener_isbn(self):
        return self.__isbn

    # Método setter
    def establecer_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    # Método setter
    def establecer_autor(self, nuevo_autor):
        self.__autor = nuevo_autor

    # Método mostrar detalles del objeto
    def mostrar_detalles(self):
        print(f"\nTítulo: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"ISBN: {self.__isbn}")
        print(f"Portada: {self.portada}")

# Creación del objeto con valores coherentes para un libro
libro = Libros("1984", "George Orwell", "978045", "Portada deseada")

# Imprimir atributos públicos y privados
libro.mostrar_detalles()

print("------------------------")

# Modificar el atributo encapsulado usando getter y setter
libro.establecer_titulo("Rebelión en la granja")  # setter
print(f"Título: {libro.obtener_titulo()}")  # getter
libro.establecer_autor("Orwell")  # setter
print(f"Autor: {libro.obtener_autor()}")  # getter
print(f"ISBN: {libro.obtener_isbn()}")  # getter
print(f"Portada: {libro.portada}")  # público
