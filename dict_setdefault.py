fruit = {
    "type": "apple",
    "variety": "Gala",
    "calories": 80
}
print(fruit)


# dict.setdefault(key, default_value) gets the value of the key.
# Since the value of the key "variety" has already been set,
# this does NOT set it to the new specified value.
m = fruit.setdefault("variety", "Fuji")
print(m)


# dict.setdefault(key, default_value) gets the value of the key.
# Since the value of the key "color" has not already been set,
# this DOES set it to the new specified value.
c = fruit.setdefault("color", "red")
print(c)


# dict.setdefault(key) gets the value of the key.
# Since the value of the key "origin" has not already been set,
# this DOES set it to None, since no new value was specified.
o = fruit.setdefault("origin")
print(o)

print(fruit)


