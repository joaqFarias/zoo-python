
class animal:
    def __init__(self, nombre: str, edad: int, reino: str, especie: str):
        self.nombre = nombre
        self.edad = edad
        self.reino = reino
        self.especie = especie
        self.salud = 100
        self.felicidad = 100

    def alimentar(self):
        self.salud += 5
        self.felicidad += 10
        print(f"\n{self.nombre} dice: ñam ñam...")
        return self

    def regañar(self):
        self.salud -= 2
        self.felicidad -= 20
        print(f"\n{self.nombre} dice: :(")
        return self

    def reproducir(self, zoo: object):
        self.salud += 10
        self.felicidad += 10
        print(f"\n{self.nombre} dice: <3")
        print(f"Felicidades {self.nombre} ha parido una cria!")
        nombre_cria = input(f"Por favor ingrese el nombre de la cria\n")
        edad_cria = 0
        zoo.add_animal(nombre_cria, edad_cria, self.reino, self.especie)
        print(f"EL nombre de la cria es : {nombre_cria} y su edad es {edad_cria}")
        return self

    def sacrificar(self, zoo: object):
        print(f"\n{self.nombre} dice: ...")
        for ani in range(len(zoo.animales[self.reino][self.especie])):
            if self.nombre == zoo.animales[self.reino][self.especie][ani].nombre:
                zoo.animales[self.reino][self.especie].pop(ani)
        print(f"Se sacrifico a {self.nombre} :(")

    def __str__(self):
        return f"Nombre: {self.nombre}, edad: {self.edad}, salud: {self.salud}, felicidad: {self.felicidad}"
