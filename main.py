# from reinos.mamiferos import *
# no funciona cuando pongo lo modulos en otra carpeta !!! :(

from mamiferos import *
from anfibios import *
from aves import *
from peces import *
from reptiles import *


class Zoo:
    def __init__(self, zoo_nombre):
        self.animales = {}
        self.animales["mamifero"] = {} 
        self.animales['mamifero']['oso'] = []
        self.animales['mamifero']['lobo'] = []
        self.animales['mamifero']['elefante'] = []
        self.animales['mamifero']['leon'] = []
        self.animales['mamifero']['jirafa'] = []

        self.animales["anfibio"] = {}
        self.animales["anfibio"]['sapos comun'] = []
        self.animales["anfibio"]['sapos gigante'] = []
        self.animales["anfibio"]['salamandra'] = []

        self.animales["ave"] = {}
        self.animales["ave"]['condor'] = []
        self.animales["ave"]['avestruz'] = []
        self.animales["ave"]['pinguino'] = []

        self.animales["pez"] = {}
        self.animales["pez"]['tiburon'] = []
        self.animales["pez"]['pez payaso'] = []
        self.animales["pez"]['salmone'] = []

        self.animales["reptil"] = {}
        self.animales["reptil"]['gecko'] = []
        self.animales["reptil"]['cocodrilo'] = []
        self.animales["reptil"]['tortuga'] = []
        self.animales["reptil"]['vivora'] = [] 

        self.nombre = zoo_nombre

    def add_animal(self, nombre: str, edad: int, reino: str, especie: str) -> object:
        # mamiferos
        if especie == 'oso':
            self.animales[reino][especie].append(oso(nombre, edad, reino, especie))
        elif especie == 'lobo':
            self.animales[reino][especie].append(lobo(nombre, edad, reino, especie))
        elif especie == 'elefante':
            self.animales[reino][especie].append(elefante(nombre, edad, reino, especie))
        elif especie == 'leon':
            self.animales[reino][especie].append(leon(nombre, edad, reino, especie))
        elif especie == 'jirafa':
            self.animales[reino][especie].append(jirafa(nombre, edad, reino, especie))
        # anfibios
        elif especie == 'sapo comun':
            self.animales[reino][especie].append(sapo_comun(nombre, edad, reino, especie))
        elif especie == 'sapo gigante':
            self.animales[reino][especie].append(sapo_gigante(nombre, edad, reino, especie))
        elif especie == 'sapo comun':
            self.animales[reino][especie].append(salamandra(nombre, edad, reino, especie))
        # aves
        elif especie == 'condor':
            self.animales[reino][especie].append(condor(nombre, edad, reino, especie))
        elif especie == 'avestruz':
            self.animales[reino][especie].append(avestruz(nombre, edad, reino, especie))
        elif especie == 'pinguino':
            self.animales[reino][especie].append(pinguino(nombre, edad, reino, especie))
        # peces
        elif especie == 'tiburon':
            self.animales[reino][especie].append(tiburon(nombre, edad, reino, especie))
        elif especie == 'pez payaso':
            self.animales[reino][especie].append(pez_payaso(nombre, edad, reino, especie))
        elif especie == 'salmon':
            self.animales[reino][especie].append(salmon(nombre, edad, reino, especie))
        # reptiles
        elif especie == 'gecko':
            self.animales[reino][especie].append(gecko(nombre, edad, reino, especie))
        elif especie == 'cocodrilo':
            self.animales[reino][especie].append(cocodrilo(nombre, edad, reino, especie))
        elif especie == 'tortuga':
            self.animales[reino][especie].append(tortuga(nombre, edad, reino, especie))
        elif especie == 'vivora':
            self.animales[reino][especie].append(vivora(nombre, edad, reino, especie))
        else:
            print("ERROR: ingrese reino animal o tipo de animal correcto.")
            return
        print("\nEl animal fue agregado correctamente!")
        return self
    
    def mostrar_info(self):
        print("-"*30, self.nombre, "-"*30)
        for reino in self.animales.values():
            for especie in reino.values():
                for idx_animal in range(len(especie)):
                    print(especie[idx_animal])

def ingrese_reino_especie() -> str:
    reino_animal = input('Ingrese el reino del animal(mamifero, anfibio, ave, pez o reptil):   ')
    if reino_animal == 'mamifero':
            especie_animal = input('Ingrese especie del animal(oso, lobo, elefante, leon, jirafa):   ')
    elif reino_animal == 'anfibio':
        especie_animal = input('Ingrese especie del animal(sapo comun, sapo gigante, salamdra):   ')
    elif reino_animal == 'ave':
        especie_animal = input('Ingrese especie del animal(condor, avestruz, pinguino):   ')
    elif reino_animal == 'pez':
        especie_animal = input('Ingrese especie del animal(tiburon, pez payaso, salmon):   ')
    elif reino_animal == 'reptil':
        especie_animal = input('Ingrese especie del animal(gecko, cocodrilo, tortuga, vivora):   ')
    else:
        print("ERROR: Ingrese reino animal valido.")
        return False, False
    return reino_animal, especie_animal

def encontrar_animal():
    reino_animal, especie_animal =  ingrese_reino_especie()
    if reino_animal == False:
        return False
    for ani in range(len(zoo1.animales[reino_animal][especie_animal])):
        print(f"{ani}. {zoo1.animales[reino_animal][especie_animal][ani].nombre}")
    return True

if __name__ == "__main__":
    print("-"*30," Bienvenido al administrador de zoologicos! ", "-"*30)
    nombre_zoo = input("\nIngrese nombre del zoologico:\n")
    zoo1 = Zoo('Zoologico ' + str(nombre_zoo))
    salir = False
    while salir != "q":
        print(f"\nPor favor, eliga una opcion:")
        print("1. Agregar animal")
        print("2. Alimentar animal")
        print("3. Regañar animal")
        print("4. reproducir animal")
        print("5. Sacrificar animal")
        print("6. Mostrar informacion de zoologico")
        print("7. Salir\n")
        opcion = input()

        if int(opcion) == 1: # agregar
            nombre_animal = input('Ingrese el nombre del animal:   ')
            edad_animal = input('ingrese la edad del animal:   ')
            reino_animal, especie_animal =  ingrese_reino_especie()
            if reino_animal == False:
                continue
            zoo1.add_animal(nombre_animal, edad_animal, reino_animal, especie_animal)

        elif int(opcion) == 2: # alimentar
            animal_encontrado = encontrar_animal()
            if animal_encontrado == False:
                continue
            num_animal = input('Ingrese numero del animal que desea alimentar:  ')
            zoo1.animales[reino_animal][especie_animal][int(num_animal)].alimentar()

        elif int(opcion) == 3: # regañar
            animal_encontrado = encontrar_animal()
            if animal_encontrado == False:
                continue
            num_animal = input('Ingrese numero del animal que desea regañar:  ')
            zoo1.animales[reino_animal][especie_animal][int(num_animal)].regañar()

        elif int(opcion) == 4: # reproducir
            animal_encontrado = encontrar_animal()
            if animal_encontrado == False:
                continue
            num_animal = input('Ingrese numero del animal que desea reproducir:  ')
            zoo1.animales[reino_animal][especie_animal][int(num_animal)].reproducir(zoo1)

        elif int(opcion) == 5: # sacrificar
            animal_encontrado = encontrar_animal()
            if animal_encontrado == False:
                continue
            num_animal = input('Ingrese numero del animal que desea sacrificar:  ')
            zoo1.animales[reino_animal][especie_animal][int(num_animal)].sacrificar(zoo1)

        elif int(opcion) == 6: # mostrar informacion
            zoo1.mostrar_info()

        elif int(opcion) == 7: # salir
            print("\nGracias por visitarnos!")
            break

        else:
            print("Ingrese opcion correcta!") 