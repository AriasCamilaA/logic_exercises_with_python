# Escriba una clase de Python para implementar pow(x, n)

class CambiarBase():
    """Clase para cambiar de base 2, 3, 4, 5, 6, 7, 8 y 9 a base 10
    """
    base_old = None
    base_new = 0
    base = None

    def __init__(self, _base_old:int):
        """
            Constructor

        Args:
            _base_old (int): numero que deseamos convertir
        """
        self.base_old = _base_old

    def cambiar(self, _base:int):
        """
            Metodo para cambiar de base

        Args:
            _base (int): Base en la que se ingresó el número
        """
        self.base = _base
        p = 0
        for i in str(self.base_old):
            self.base_new += int(i) * pow(self.base, p)
            p += 1

    def mostrar_conversion(self):
        """Mostrar la conversión
        """
        print(f"{self.base_old} base {self.base} es igual a {self.base_new} en base 10")
        
        
num = CambiarBase(111)
num.cambiar(3)
num.mostrar_conversion()
