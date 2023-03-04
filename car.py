class Car:
#pass
    def __int__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def drive(self):
        print("this car is driving")
    def stop(self):
        print("this car is stopping")