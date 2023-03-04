class fruits:  #Class declaration
    Name="Apple"
    No="A1"
    def deisplay(self):  #Instance method
        print(self.Name, self.No)


class employee:
    salutation = "Wellcome All"  # class instance attribute

    def __init__(self):
        self.Name = 'Kokila'
        self.Id = 101

    def display(self):  # class instance method
        print("Employee Name: %s \n Id: %d" % (self.Name, self.Id))


Emp = employee()
print(Emp.salutation)  # call instance attribute
Emp.display()



