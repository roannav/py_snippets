lst = [ 1, 2, 3]
print(f"The original lst = {lst}")

lst2 = lst.copy()
lst3 = lst

lst[0] = 99
print("\nAfter changing the first element:")
print(f"The original lst = {lst}")

print(f"\nlst2 = lst.copy() .... (so lst2 is a real copy) ......... = {lst2}")
print(f"lst3 = lst  .......... (so lst3 is just a reference) .... = {lst3}")


# lst3 = lst   is NOT a copy;  lst3 is only getting a reference to lst.
# Now lst and lst3 are referring to the SAME object, so changing one 
# will also change the other.

# 2 ways to make a copy of a list:
# 1) list() constructor
# 2) list.copy() method
# It's similar for dictionaries.

# copy the list with the list() constructor
lst4 = list(lst)
print(lst4)

# copy the list with the copy() method
lst5 = lst.copy()
print(lst5)
