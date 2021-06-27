import animales as ra

class mamifero(ra.animal):
    def parir(self):
        print(f"Felicidades {self.nombre} ha parido una cria!")
        nombre_cria = input(f"Por favor ingrese el nombre de la cria\n")
        print(f"EL nombre de la cria es : {nombre_cria}")
        

class oso(mamifero):
    def rugir(self):
        print("AHGGG!")

class lobo(mamifero):
    def __init__(self):
        pass

class elefante(mamifero):
    def __init__(self):
        pass

class leon(mamifero):
    def __init__(self):
        pass

class jirafa(mamifero):
    def __init__(self):
        pass