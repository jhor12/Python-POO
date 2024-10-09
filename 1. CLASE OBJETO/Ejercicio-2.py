#Defino la clase 
class Animales:
    #Metodo constructor
    def __init__(self, nombre, tamaño, años, color):
        #Defino  los atributos de instancia de la clase
        self.nombre = nombre
        self.tamaño = tamaño
        self.años = años
        self.color = color

    #Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información del Animal")    
        print("Nombre: " +self.nombre)
        print("tamaño: " +self.tamaño)
        print("años: " +self.años)
        print("color: " +self.color)
        print("-------------------------------------------")

    def especie(self):
        #defino el atributo privado energia solo para metodo encender
        print("mariposa, conejo, serpiente")
        self.animal = (input("Digite el nombre de algunos de los animales mostrados en pantalla:" )) 
        #Evaluamos si tiene carga el celular 
        if self.animal == "mariposa" :
            print("El animal "+ self.animal+ " es de especie Lepidópteros") 
        elif self.animal == "conejo" :
            print("El animal "+ self.animal+ " es de especie Mamífero")
        elif self.animal == "serpiente" :
            print("El animal "+ self.animal+ " es de especie Reptil")        
            print("------------------------------------------------")
        else:
            print("El animal digitado no se encuentra")    

#Creamos los objetos
animal1 = Animales("MARIPOSA", "16 CM", "1 ", "AZUL")
animal2 = Animales("CONEJO", "22 CM", "2", "BLANCO")
animal3 = Animales("SERPIENTE", "32 CM", "3", "VERDE")


#Mostrar los detalles de cada objeto
animal1.mostrar_detalles()
animal2.mostrar_detalles()
animal3.mostrar_detalles()
animal1.especie()