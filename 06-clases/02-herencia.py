class Npc():
    """
        Clase padre, para los personajes no jugadores o personajes no jugables
    """

    nombre = 0

    def __init__(self, _nombre:str):
        """Constructor para inicializar el nombre del NPC

        Args:
            _nombre (str): Nombre del NPC
        """
        self.nombre = _nombre

    def saludar(self):
        print(f'Hola mi nombre es {self.nombre}')

    def descripcion(self):
        print("Soy un NPC")


class Granjero(Npc):

    mision = None

    def __init__(self, _nombre:str, _mision:str):
        self.nombre = _nombre
        self.mision = _mision

    def tarea(self):
        print(f'Mi misión será {self.mision}')

class Heroe(Npc):

    def msg(self):
        print(f'Yo {self.nombre} soy un gran heroe')

class Monstruo(Npc):
    atk = None
    def __init__(self, _nombre:str, _atk:str):
        self.nombre = _nombre
        self.atk = _atk
    
    def atacar(self):
        print(f'{self.nombre} usa {self.atk} para atacar al heroe')


print("---------------")
granjero = Granjero("Malon", "Sembrar vegetales para la cosecha")
granjero.descripcion()
granjero.saludar()
granjero.tarea()
print("---------------")
heroe = Heroe("Link")
heroe.descripcion()
heroe.saludar()
heroe.msg()
print("---------------")
monstruo = Monstruo("Slime", "lava")
monstruo.descripcion()
monstruo.saludar()
monstruo.atacar()

