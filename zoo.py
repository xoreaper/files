class Animal:
    def __init__(self, name, species, habitat):
        self.name = name
        self.species = species
        self.habitat = habitat

    def make_sound(self):
        print("Generic animal sound")


class Mammal(Animal):
    def make_sound(self):
        print("Mammal sound: Roar!")


class Amphibian(Animal):
    def make_sound(self):
        print("Amphibian sound: Croak!")


class Reptile(Animal):
    def make_sound(self):
        print("Reptile sound: Hiss!")


def animal_in_zoo_sound(animal_obj):
    animal_obj.make_sound()


if __name__ == "__main__":

    lion = Mammal("Leo", "Lion", "Grasslands")
    frog = Amphibian("Freddy", "Frog", "Pond")
    snake = Reptile("Sam", "Snake", "Jungle")

    animal_in_zoo_sound(lion)
    animal_in_zoo_sound(frog)
    animal_in_zoo_sound(snake)
