# Escriba una clase que represente un carro con métodos y atributos

class Carro:

    """
        Define un carro con placa, color, modelo, marca y velocidad
    """

    placa = None
    color = None
    modelo = None
    marca = None
    velocidad = 0
    
    def __init__(self,_placa:str, _color:str, _modelo:str, _marca:str):
        self.placa = _placa
        self.color = _color
        self.modelo = _modelo
        self.marca = _marca
    
    def arrancar(self):
        """
            Metodo para que el carro arranque
        """
        print("RUN RUN RUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUN")

    def acelerar(self,_velocidad):
        """
            Acelerar la velocidad según lo que se le ingrese en km/h

        Args:
            _velocidad (_type_): km/h que aumenta la velocidad
        """
        self.velocidad += _velocidad
        print(f"Acelero a {self.velocidad}km/h")

    def frenar(self):
        """
            Reduce la velocidad a 0
        """
        print("Ha frenado")
        self.velocidad = 0

mi_carro = Carro("ABC-123","Rojo","Corona","Toyota")
mi_carro.arrancar()
desc = f"""
Placa: {mi_carro.placa}
Color: {mi_carro.color}
Modelo: {mi_carro.modelo}
Marca: {mi_carro.marca}
"""
print(desc)
mi_carro.acelerar(100)
mi_carro.acelerar(50)
print(f"Velocidad actual: {mi_carro.velocidad}")
mi_carro.frenar()
print(f"Velocidad actual: {mi_carro.velocidad}")


