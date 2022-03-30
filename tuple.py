# you don't even need the () to define a tuple
tuple0 = 4, 2, 3, 1, 5


# if the tuple has only 1 item, you have to ADD A COMMA at the end
tuple1 = ("one",)
print(type(tuple1))

# w/out the comma, python is just going to process the ()
# as a grouping operator.  So the () will disappear.
s = ("nope")
print(type(s))
i = (1)
print(type(i))
b = (False)
print(type(False))

# Create a tuple with the tuple() constructor
# Use double set of parenthesis   (())
tuple2 = tuple(("one", 2, True, {"name": "Mary"}, {'a','b'}))
print(tuple2)
print(type(tuple2))

# This won't work because tuple expects exactly 0 or 1 arguments!
# opps = tuple("one", 2, True, {"name": "Mary"}, {'a','b'})

# when a tuple is created and assigned a value,
# that is called PACKING a tuple
tuple3 = (45, 78)

# The reverse, using a tuple to assign variables,
# is called UNPACKING a tuple.
x, y = tuple3
print(f"\nx is {x} and y is {y}")


tuple4 = "blue", "red", "yellow", "orange"
# fav_color will get the first item in the tuple
# other_colors will get assigned the rest, because of the *
fav_color, *other_colors = tuple4
print(f"\noriginal tuple is {tuple4}")
print(f"fav_color is {fav_color}")
print(f"other_colors are {other_colors}")
print(f"other_colors is a {type(other_colors)}")

tuple5 = "blue", "red", "yellow", "orange", "violet", "purple", "green"
# fav_color will get the first item in the tuple
# other_colors will get assigned the rest, because of the *
fav_color, *other_colors, second_least_fav_color, least_fav_color = tuple5
print(f"\noriginal tuple is {tuple5}")
print(f"fav_color is {fav_color}")
print(f"other_colors are {other_colors}")
print(f"other_colors is a {type(other_colors)}")
print(f"second_least_fav_color is {second_least_fav_color}")
print(f"least_fav_color = is {least_fav_color}")

# Create a new tuples quickly using + or *
# NOTE: no tuple is being changed; we are just creating a NEW tuple
tuple6 = tuple3 + tuple4
print(tuple6)

tuple7 = tuple3 * 2
print(tuple7)

print(f"Length of tuple is {len(tuple7)}")
print(f"Count of the number 45 in tuple7 is {tuple7.count(45)}")
print(f"Index (aka first occurrance) of the number 45 in tuple7 is {tuple7.index(45)}")

x_vals = (4,8,9,2,1)
# NOTE: to make a tuple comprehension, use need to use the word tuple

# no "tuple"  ==> you get a <class 'generator'> 
scaled_gen = (x * 10 for x in x_vals)
print(type(scaled_gen))
print(scaled_gen)

scaled = tuple(scaled_gen)
print(type(scaled))
print(scaled)
