
d = {'apple': 60, 'banana': 45, 'cherry': 77, 'durian': 126, 'elderberry': 3, 'strawberry': 130}
print("Current Inventory")
print(d)

# find items with quantity less than 50
# dictionary comprehension with a conditional
need_to_reorder = { k:v for k,v in d.items() if v<50 }
print("\nNeed to reorder these items")
print(need_to_reorder)

# find items with quantity >= 50 and is a berry (has berry in the name)
# dictionary comprehension with 2 conditionals
lots_of_berries = { k:v for k,v in d.items() if v>=50 if "berry" in k }
print("\nWe have lots of these berries.")
print(lots_of_berries)


# create a dictionary that for each item, the value is true/false 
# ie whether it needs to be reordered, because quantity < 50
print("\nReorder?: True or False")
reorder = { k:(v<50) for k,v in d.items() }
print(reorder)

# create a dictionary that for each item, the value is "reorder"/"enough" 
# ie whether it needs to be reordered, because quantity < 50
print("\nReorder?: reorder or enough")
reorder2 = { k:"reorder" if v<50 else "enough" for k,v in d.items()}
print(reorder2)

