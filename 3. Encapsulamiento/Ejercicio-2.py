#Clase Producto con atributos encapsulados o privados
class Producto:
    #metodo constructor
    def __init__(self, nombre, precios, cantidad, categoria):
        self.__nombre = nombre  # privado
        self.__precios = precios  # privado
        self.cantidad = cantidad  # público
        self.categoria = categoria  # público

    #metodo getter
    def obtener_nombre(self):
        return self.__nombre

    #metodo getter
    def obtener_precios(self):
        return self.__precios

    #metodo setter
    def establecer_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    #metodo setter
    def establecer_precios(self, nuevo_precios):
        self.__precios = nuevo_precios

    #metodo mostrar detalles del objeto
    def mostrar_detalles(self):
        print(f"\nNombre: {self.__nombre}")
        print(f"Precios: {self.__precios}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Categoría: {self.categoria}")

# Creación del objeto con valores coherentes para un producto
producto = Producto("Laptop", 1500, 10, "Electrónica")

# Imprimir atributos públicos y privados
producto.mostrar_detalles()

print("------------------------")

# Modificar el atributo encapsulado usando getter y setter
producto.establecer_nombre("Smartphone")  # setter
print(f"Nombre: {producto.obtener_nombre()}")  # getter
producto.establecer_precios(800)  # setter
print(f"Precios: {producto.obtener_precios()}")  # getter
print(f"Cantidad: {producto.cantidad}")  # público
print(f"Categoría: {producto.categoria}")  # público

