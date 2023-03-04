class car :
    def turn_on(self):
        print("you start the engine")
        return self
    def drive(self):
        print("you drive the car")
        return self
    def brake(self):
        print("you are step on brakes ")
        return self
    def turn_off(self):
        print("you are turned off the engine")
        return self
car=car()
car.turn_on().drive()
car.brake().turn_off()
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
