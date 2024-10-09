# Clase padre Profesiones
class Profesiones:
    def __init__(self, nombre, edad, especialidad):
        self.nombre = nombre
        self.edad = edad
        self.especialidad = especialidad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Especialidad: {self.especialidad}")

    def trabajar(self):
        pass  # Método que será sobrescrito por las clases hijas

# Clase hija Médico
class Medico(Profesiones):
    def __init__(self, nombre, edad, especialidad, hospital):
        super().__init__(nombre, edad, especialidad)
        self.hospital = hospital

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Hospital: {self.hospital}")

    def trabajar(self):
        print(f"{self.nombre} está atendiendo pacientes en el hospital {self.hospital}.")

# Clase hija Ingeniero
class Ingeniero(Profesiones):
    def __init__(self, nombre, edad, especialidad, campo):
        super().__init__(nombre, edad, especialidad)
        self.campo = campo

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Campo de trabajo: {self.campo}")

    def trabajar(self):
        print(f"{self.nombre} está diseñando y supervisando proyectos en el campo de {self.campo}.")

# Clase hija Docente
class Docente(Profesiones):
    def __init__(self, nombre, edad, especialidad, asignatura):
        super().__init__(nombre, edad, especialidad)
        self.asignatura = asignatura

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Asignatura: {self.asignatura}")

    def trabajar(self):
        print(f"{self.nombre} está enseñando la asignatura de {self.asignatura}.")

# Función que muestra la información y el trabajo de cualquier profesional
def mostrar_informacion(profesion):
    profesion.mostrar_info()
    profesion.trabajar()

# Instancias de cada clase
objeto_medico = Medico("Dr. Roberto", 48, "Cardiología", "Hospital Central")
objeto_ingeniero = Ingeniero("Ing. Jorge", 38, "Civil", "Construcción")
objeto_docente = Docente("Prof. Elias", 50, "Matemáticas", "Álgebra")

# Llamado al método mostrar_info y trabajar para cada objeto
mostrar_informacion(objeto_medico)
mostrar_informacion(objeto_ingeniero)
mostrar_informacion(objeto_docente)
