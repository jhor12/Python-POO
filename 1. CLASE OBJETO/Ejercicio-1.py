#Defino la clase 
class Celular:
    #Metodo constructor
    def __init__(self, nombre, marca, imei, ram, bateria):
        #Defino  los atributos de instancia de la clase
        self.nombre = nombre
        self.marca = marca
        self.imei = imei
        self.ram = ram
        self.bateria = bateria

    #Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información del Celular")    
        print("Nombre: " +self.nombre)
        print("Marca: " +self.marca)
        print("imei: " +self.imei)
        print("ram: " +self.ram)
        print("bateria: " +self.bateria)
        print("-------------------------------------------")

    def encender(self):
        #defino el atributo privado energia solo para metodo encender
        self.energia = int(input("Digite el valor de la carga: " )) 
        #Evaluamos si tiene carga el celular 
        if self.energia >0 :
            print("El celular "+ self.nombre+ " se puede encender") 
            print(f"||||||||| {self.energia} % de carga") 
            print("------------------------------------------------")
        else:
            print("El celular "+self.nombre+ "no se puede encender")

    def apagar(self):
        #Defino el atributo pribado carga solo para el metodo apagar
        self.off = int(input("Digite el valor de la carga: " ))
        #Evaluamos que cantidad de carga tiene el celular
        if self.off >0:
            print("El celular "+ self.nombre+ "esta pronto en apagarse")
            print(f"le falta un ||||||| {self.off} % para apagarse")
            print("-------------------------------------------------")
        else:
            print(f"El celular {self.nombre } esta en 0% se va a apagar")   

#Creamos los objetos
celular1 = Celular("HUAWEI Y9", "HUAWEI", "92593", "160", "6000 MAH")
celular2 = Celular("OPPO RENO 7", "OPPO", "63952", "256", "2000 MAH")
celular3 = Celular("MOTOROLA G60", "MOTOROLA", "49627", "128", "7000 MAH")
celular4 = Celular("HONOR.MAGIC 6", "HONOR", "336924", "256", "8000 MAH")
celular5 = Celular("RELAME C55", "RELAME", "28574", "200", "6000 MAH")


#Mostrar los detalles de cada objeto
celular1.mostrar_detalles()
celular1.encender()
celular2.mostrar_detalles()
celular2.apagar()
celular3.mostrar_detalles()
celular4.mostrar_detalles()
celular5.mostrar_detalles()


