capitals={'usa':'washington DC','india':'newdelhi','china':'begium','russia':'moscow'}
print(capitals)
print(capitals["india"])
print(capitals.get('germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key,values in capitals.items():
    print(key,values)

capitals.update({'germany':'berlin'})
print(capitals)
capitals.pop('china')
print(capitals)
capitals.clear()
print(capitals)