class animal:
    alive = True

    def eat(self):
        print("this animal is eating")

    def slumber(self):
        print("this animal is sleeping")
class rabbit(animal):
    def run(self):
        print("this rabbit is runnng")
class fish(animal):
    def swim(self):
        print("this animal is swimming")
class hawk(animal):
    def fly(self):
        print("this hawk is flying")

rabbit=rabbit()
fish=fish()
hawk=hawk()
print(rabbit.alive)

rabbit.run()
rabbit.eat()
rabbit.slumber()
print(fish.alive)
fish.swim()
fish.eat()
fish.slumber()
print(hawk.alive)
hawk.fly()
hawk.eat()
hawk.slumber()