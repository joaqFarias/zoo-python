from reinos import mamiferos as ma
from reinos import animales as ra


class Zoo:
    def __init__(self, zoo_nombre):
        self.animales = {}
        self.animales["mamiferos"] = [] 
        self.animales["anfibios"] = []
        self.animales["aves"] = []
        self.animales["peces"] = []
        self.animales["reptiles"] = []

        self.nombre = zoo_nombre

    def add_animal(self, nombre: str, reino: str, tipo: str) -> object:
        
        try:
            self.animales[reino].append(tipo(nombre))
        except:
            TypeError(print("ingrese reino animal o tipo de animal correcto."))
        return self
    
    def print_all_info(self):
        print("-"*30, self.nombre, "-"*30)
        for reino in self.animales.value():
            reino.display_info()

if __name__ == "__main__":
    zoo1 = Zoo("Zoologico Lucas")
    #zoo1.add_animal("Pedro el oso", "mamifero", "oso")
    oso1 = ma.oso("Pedro el oso", 5)   