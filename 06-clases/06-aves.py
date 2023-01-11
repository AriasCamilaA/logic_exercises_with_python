# Escriba un clase padre llamada Ave que herede a clases hijas con tipos de aves

class Ave():
    """
        Clase padre que contiene a Palomas (Pigeons) y pinguinos (Penguins)
    """
    nombre = None

    def __init__(self, _nombre:str):
        self.nombre = _nombre

    def caminar(self):
        print(f"{self.nombre} esta caminando")

class Pigeon(Ave):
    """
        Clase hija de clase Ave
    """
    def volar(self):
        print(f"{self.nombre} esta volando por los cielos")

    def robar(self):
        print(f"{self.nombre} esta robando comida")

class Penguin(Ave):
    """
        Clase hija de clase Ave
    """
    def deslizarce(self):
        print(f"{self.nombre} esta deslizandose por el hielo")
    
print("------------------------------")
ave_1 = Pigeon("Ramira")
ave_1.caminar()
ave_1.volar()
ave_1.robar()
print("------------------------------")
ave_2 = Penguin("Paco")
ave_2.caminar()
ave_2.deslizarce()
