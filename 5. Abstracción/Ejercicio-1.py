"""
Crea una clase abstracta Empleado con un método abstracto calcular_salario(). 
Luego, crea dos clases concretas EmpleadoTiempoCompleto y 
EmpleadoPorHoras que implementen calcular_salario() de manera distinta.
"""

from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, meses_trabajados, salario_mensual):
        self.meses_trabajados = meses_trabajados
        self.salario_mensual = salario_mensual

    def calcular_salario(self):
        return self.meses_trabajados * self.salario_mensual

class EmpleadoPorHoras(Empleado):
    def __init__(self, horas_trabajadas, tarifa_por_hora):
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora

# Uso de las clases
empleado_tiempo_completo = EmpleadoTiempoCompleto(8, 60000)  # 8 meses, salario de 60000 por mes
print(f"Empleado por tiempo completo: {empleado_tiempo_completo.calcular_salario()}")

empleado_por_horas = EmpleadoPorHoras(120, 16000)  # 120 horas trabajadas, tarifa de 16000 por hora
print(f"Empleado por horas: {empleado_por_horas.calcular_salario()}")
