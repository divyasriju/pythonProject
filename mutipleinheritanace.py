class organism:
    alive =True
class animal(organism):
    def eat(self):
        print("this animal is eating")
class dog(animal):

    def bark(self):
        print("this animal is barking")
D=dog()
print(D.alive)
D.eat()
D.bark()