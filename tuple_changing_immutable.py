# Tuples are immutable
# so if you need to change the tuple, 
# you need to create a new tuple.

colors = ('red', 'green', 'aqua')
print(colors)

colors_list = list(colors)
colors_list[2] = 'blue'
# or modify the list some other way such as calling append(), insert(),
# extend(), clear(), pop(), remove(), sort() or reverse() on the list.
colors = tuple(colors_list)
print(colors)

# append a tuple using the += operator
colors += ('yellow', 'orange', 'purple')
print(colors)

