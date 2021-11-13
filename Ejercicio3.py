class Animal:
    def __init__(self, animal, clase_pertenece, lo_que_come):
        self.animal = animal
        self.clase = clase_pertenece
        self.tipo = lo_que_come
    
    def animalDetails(self):
        print("Animal:", self.animal)
        print("Clase:", self.clase)
        print("Aimentacion:", self.tipo)

#Aqui se añaden cosas como en el anterior y ocuure magia

animal1 = Animal("perro", "mamifero", "omnivoro")
animal1.animalDetails()