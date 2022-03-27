# When this file was originally named 'random.py', I got this error...
# ImportError: cannot import name 'choice' from 'random' (../random.py).
# It was trying to find choice defined within this file itself,
# rather than the official random module.

# random.choice() will return a random item from the given sequence. 
# random.choice() can take a sequence, such as a list, tuple, range, 
# or string as an argument.
# To choose a random item from a dictionary or set,
# first convert it to a list.

from random import choice

print(choice(["jazz", "pop", "classical"]))

print(choice("Given a string, random.choice() will return a single letter"))

print(choice(range(10)))  # returns a random number from 0..9

# to choose a random item from a dictionary...
# first choose a random key from the dictionary
d = { "apple": "red", "banana": "yellow", "mango": "orange"}
key = choice(list(d))
print(f"You choose {key} which is {d[key]}")

# to choose a random item from a set,
# first convert it to a list.
# Otherwise, you get TypeError: 'set' object is not subscriptable
set1 = {"apple", "banana", "mango"}
print(choice(list(set1)))
