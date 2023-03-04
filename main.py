#name="Divya.Raghavan"
#print(type(name))
#print(" hello ,"+name)
#print("my name is {}".format(name))
first_name = "Divya"
last_name = "Raghavan"
full_name = first_name+last_name
print ("hello "+full_name)
print("hello :%s" %full_name)
print(type(full_name))
age=21
#age=age+1
age+=2
print(age)
print(type(age))
print("your age is "+str(age)+" years old ")
print("your age is {} years old".format(age))
print(f"your age is {age} years old")
print("your age is %d"% age ,"year old ")

print(len(full_name))
print(len(str(age)))
print(full_name.index("a"))
print(full_name.find("D"))
print(full_name.capitalize())
print(full_name.upper())
print(full_name.lower())
print(full_name.count("a"))
print(full_name.replace("DivyaRaghavan","Sreyasriju"))
print(full_name.isalpha())
print(full_name.isdigit())
x=1
y=2.7
z="3"
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
#z=int(z)
print(z*3)
print("x is :"+str(x))
print("z is :"+z)
name,age,attractive="divya",38,"yes"
print(name,age,attractive)
a=b=c=30
print(a)
height=27.5
print(height)
print(type(height))
print("your height is "+str(height)+"in cms")
print("your height is {} in cms".format(height))
human=True
print("you are a human :"+str(human))

name=input("enter your name:")
print(" hello "+name)

age=int(input("enter your age is :"))
print("your age is "+str(age))
print("your are {} years old".format(age))
print(f"your are {age} years old")

height=float(input("enter your height in cm :"))
print("your height is "+str(height)+"in cms")
print("your height is {} in cms".format(height))
