# dict.fromkeys( iterable_with_keys, <value>)
# value parameter is optional.
# Though you have a list of keys, there is only 1 value (or no value).
# If no value is specified, then it will be None by default.
# The iterable_with_keys can be a list, set, tuple, dictionary, range

names = ["Amy", "Brent", "Carin", "Dave", "Elise"]

d = dict.fromkeys(names, 1)
print("d:", d)

d2 = dict.fromkeys(names)
print("d2:", d2)


colors = {"red", "blue", "yellow"}

d3 = dict.fromkeys(colors, 1)
print("d3:", d3)

d4 = dict.fromkeys(colors)
print("d4:", d4)

d5 = dict.fromkeys(d4, 99)
print("d5:", d5)

d6 = dict.fromkeys(range(5))
print("d6:", d6)


# NOTE: Can use either the "dict" keyword or some instance variable name 
# for the dictionary.
# dict.fromkeys( iterable_with_keys, <value>)  will still work.
# Whatever was in the dictionary instance will be ignored.
d7 = d5.fromkeys(range(5))
print("d7:", d7)
print("d5:", d5)
