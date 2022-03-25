
# NOTE: map() does not modify the original list that was passed it.
#       map() returns the modified list

# NOTE: map() returns a map object, 
#       so wrap list() around the map() 
#       to read the new list

# NOTE: abs( x)   x can be a float too; not just integer

from functools import reduce

lst = [-56, -7.8]
print(f"\nOriginal list: {lst}")
print(list(map(lambda x: abs(x), lst)))
print("mapping lambda x: abs(x)")
print(f"Original list, after map: {lst}")

lst = ["56", "78"]
print(f"\nOriginal list: {lst}")
print(list(map(lambda x: int(x), lst)))
print("mapping lambda x: int(x)")
print(f"Original list, after map: {lst}")

lst = ['blue', "RED", 'Yellow']
print(f"\nOriginal list: {lst}")
print(list(map(lambda x: x.swapcase(), lst)))
print("mapping lambda x: x.swapcase()")
print(f"Original list, after map: {lst}")

# are all words in lowercase?
lst = ['blue', "RED", 'Yellow']
print(f"\nOriginal list: {lst}")
# first map all words to whether it's lowercase or not
print("mapping lambda x: x.islower()")
m = map(lambda x: x.islower(), lst)
# then check that every result is True
print(reduce(lambda a, b: bool(a and b), m))
