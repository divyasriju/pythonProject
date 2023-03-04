utensils ={"fork","knife","spoon"}
for x in utensils:
    print(x)
print(utensils)
utensils.add("cuttlery")
print(utensils)
utensils.remove("cuttlery")
print(utensils)
utensils.clear()
print(utensils)
dishes={"bowl","plate","cup"}
utensils.update(dishes)
dishes.update(utensils)
dinner_table=utensils.union(dishes)
for x in dinner_table:
    print(x)
utensils.add("napkin")
print(utensils.difference(dishes))
print(dishes.difference(utensils))
print(utensils.intersection(dishes))