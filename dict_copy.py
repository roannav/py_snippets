d = {
  "first_name": "Joan",
  "last_name": "Chen",
  "age": 64
}

# d2 = d   is NOT a copy; d2 is only getting a reference to d.
# Now d and d2 are referring to the SAME object, so changing one 
# will also change the other.

# 2 ways to make a copy of a dictionary:
# 1) dict() constructor
# 2) dictionary.copy() method

# copy the dictionary with the dict() constructor
d1 = dict(d)
print(d1)

# copy the dictionary with the copy() method
d2 = d.copy()
print(d2)
