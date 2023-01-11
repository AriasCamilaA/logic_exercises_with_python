# Escriba una clase de Python llamada Circle construida por un radio y dos 
# métodos que calcularán el área y el perímetro de un círculo
import math

class Circle():
    """
        Clase para crear un Círculo, para poder calcular su área y perímetro
    """
    radio = None

    def __init__(self, radio:float):
        self.radio = radio

    def area(self):
        print(f"El área del Círculo es {math.pi*self.radio**2} unidades cuadradas")
    
    def per(self):
        print(f"El perímetro del Círculo es {math.pi*self.radio*2}")
    
circulo = Circle(10)
circulo.area()
circulo.per()