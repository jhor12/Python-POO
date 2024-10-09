#Defino la clase 
class Moto:
    #Metodo constructor
    def __init__(self, modelo, marca, color, placa):
        #Defino  los atributos de instancia de la clase
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.placa = placa

    #Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información de la moto")    
        print("modelo: " +self.modelo)
        print("marca: " +self.marca)
        print("color: " +self.color)
        print("placa: " +self.placa)
        print("-------------------------------------------")

    def frenar(self):
        #Defino el atributo pribado carga solo para el metodo frenar
        self.freno = int(input("Digite del 1 al 3 que tanto freno crea que tenga su moto sabiendo que el 3 es mucho: " ))
        #Evaluamos que cantidad de freno tiene La moto
        if self.freno == 1:
            print("La moto "+ self.modelo+ " urge ponerle bandas nuevas")
        elif self.freno == 2 :
            print("La moto "+ self.modelo+ " en pocos dias es necesario cambiarle bandas")
        elif self.freno == 3 :
            print("La moto "+ self.modelo+ " aun no necesita bandas nuevas")

            print("-------------------------------------------------")
        else:
            print("El numero seleccionado no fue identificado")    

#Creamos los objetos
moto1 = Moto("BOXER S PRO", "BOXER", "NEGRO", "MFX-97A")
moto2 = Moto("BOXER CT100 KS", "BOXER", "AZUL", "FSM-92S")
moto3 = Moto("XTZ 150", "YAMAHA", "ROJO", "MFX-28B")

#Mostrar los detalles de cada objeto
moto1.mostrar_detalles()
moto2.mostrar_detalles()
moto3.mostrar_detalles()
moto1.frenar()