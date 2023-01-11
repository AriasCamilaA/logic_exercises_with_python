# Escriba una clase de Python llamada Rectangle construida por una longitud y anchura 
# y un método que calculará el área de un rectángulo

class Rectangle():
    """
        Clase para crear un rectangulo y poder calcular su área
    """
    longitud = None
    anchura = None

    def __init__(self, _longitud:float, _anchura:float):
        self.longitud = _longitud
        self.anchura = _anchura

    def area(self):
        print(f"El área del rectángulo es {self.longitud*self.anchura} unidades cuadradas")
    
rectangulo = Rectangle(10, 20)
rectangulo.area()