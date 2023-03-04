food =["sushi","pizza","hamburger","hotdog","sphagetti"]
print(food)
print(food[0])

for x in food :
    print(x)

food.append("iccream")
print(food)
food.pop(5)
print(food)
food.remove("sphagetti")
print(food)
food.insert(2,"cake")
print(food)
food.sort()
print(food)
food.clear()
print(food)

drinks=["soda","coffee","tea"]
dinner=["pizza","hamburger","hotdog"]
desserts=["cake","icecream"]
food=[drinks,dinner,desserts]
print(food)
print (food[0])
print(food[0][1])
print(food[1][2])
print(food[2][1])