from reinos.animales import *

class anfibio(animal):
    def ser_anfibio(self):
        print("Hola soy anfibio jojo")

class sapo_comun(anfibio):
    def saltar(self):
        print(f"sot el sapo {self.nombre} y salto ¡Rooaanac!")

class sapo_gigante(anfibio):
    pass

class salamandra(anfibio):
    pass
