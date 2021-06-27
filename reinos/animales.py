
class animal:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
        self.salud = 100
        self.felicidad = 100

    def alimentar(self):
        return self

    def fiebre(self):
        return self

    def reproducirse(self):
        return self

    def morir(self):
        pass
