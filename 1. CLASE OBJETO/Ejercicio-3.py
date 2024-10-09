#Defino la clase 
class Carro:
    #Metodo constructor
    def __init__(self, modelo, marca, color, placa):
        #Defino  los atributos de instancia de la clase
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.placa = placa

    #Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información del Carro")    
        print("modelo: " +self.modelo)
        print("marca: " +self.marca)
        print("color: " +self.color)
        print("placa: " +self.placa)
        print("-------------------------------------------")

    def frenar(self):
        #Defino el atributo pribado carga solo para el metodo frenar
        self.freno = int(input("Digite del 1 al 3 que tanto freno crea que tenga su carro sabiendo que el 3 es mucho: " ))
        #Evaluamos que cantidad de freno tiene el carro
        if self.freno == 1:
            print("El carro "+ self.modelo+ " urge ponerle bandas nuevas")
        elif self.freno == 2 :
            print("el carro "+ self.modelo+ " en pocos dias es necesario cambiarle bandas")
        elif self.freno == 3 :
            print("el carro "+ self.modelo+ " aun no necesita bandas nuevas")

            print("-------------------------------------------------")
        else:
            print("El numero seleccionado no fue identificado")    

#Creamos los objetos
carro1 = Carro("S-CROOS NEW", "SUZUKI", "ROJO", "XXR-882")
carro2 = Carro("SELDOS", "KIA", "AZUL", "MNW-281")
carro3 = Carro("PATROL", "NISSAN", "BLANCO", "MFX-692")

#Mostrar los detalles de cada objeto
carro1.mostrar_detalles()
carro2.mostrar_detalles()
carro3.mostrar_detalles()
carro1.frenar()