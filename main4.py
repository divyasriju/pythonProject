name=None
while not name:
    name=input("enter your name:")
    print("my name is "+name)


if (name[0].islower()):
    print(name.capitalize())
first_name=name[0:5].upper()
last_name=name[5:].lower()
last_character=name[-1]
print(last_character)
print(first_name+last_name)
