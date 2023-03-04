class prey:
    def flee(self):
        print("this animal flees")
class predator:
    def hunt(self):
        print("this animal hunts")
class rabbit(prey):
     pass
class hawk(predator):
    pass
class fish(prey,predator):
    pass

rabbit=rabbit()
hawk=hawk()
fish=fish()
rabbit.flee()
fish.hunt()
hawk.hunt()