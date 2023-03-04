from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

class car(vehicle):
    def go(self):
        print("you drive the car")
class motorbike(vehicle):
    def go(self):
        print("you ride the motorbike")

car=car()
motorbike=motorbike()

car.go()
motorbike.go()
