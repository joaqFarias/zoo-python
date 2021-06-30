from reinos.animales import *

class ave(animal):
    def volar(self):
        print("Soy un ave y me gusta volar, pero esta jaula es pequeña :(")

class condor(ave):
    pass

class avestruz(ave):
    def volar(self):
        print("Hola soy una avestruz solo corro, no vuelo")

class pinguino(ave):
    def volar(self):
        print("Hola soy un pinguino me gusta nadar, no vuelo")