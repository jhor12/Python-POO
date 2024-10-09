#Defino la clase 
class Empleado:
    #Metodo constructor
    def __init__(self, trabajo, altura, sexo, años):
        #Defino  los atributos de instancia de la clase
        self.trabajo = trabajo
        self.altura = altura
        self.sexo = sexo
        self.años = años

    #Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información del Empleado")    
        print("trabajo: " +self.trabajo)
        print("altura: " +self.altura)
        print("sexo: " +self.sexo)
        print("años: " +self.años)
        print("-------------------------------------------")

    def pago(self):
        #Defino el atributo pribado carga solo para el metodo pago
        self.pagos = (input("Digite alguna de las obsiones de trabajo: albañil, doctora, cocinera."))
        
        if self.pagos == "albañil" :
            print("El trabajo del albañil es pagado por 35000$ por dia")
        elif self.pagos == "doctora" :
            print("El trabajo de doctora es pagado por 67000$ por dia")
        elif self.pagos == "cocinera":
            print("El traajo de cocinera es pagado por 26000$ por dia")

            print("-------------------------------------------------")
        else:
            print("El trabajo digitado no fue identificado :(")        


#Creamos los objetos
empleado1 = Empleado("ALBAÑIL", "168 CM", "MASCULINO", "38")
empleado2 = Empleado("DOCTORA", "156 CM", "FEMENINO", "26")
empleado3 = Empleado("COCINERA", "163 CM", "FEMENINO", "28")

#Mostrar los detalles de cada objeto
empleado1.mostrar_detalles()
empleado2.mostrar_detalles()
empleado3.mostrar_detalles()
empleado1.pago()