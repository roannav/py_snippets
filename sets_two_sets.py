# Functions that deal with 2 sets
# 
# set1.update(set2)            # adds the elements in set2 to set1
# set1.insection_update(set2)
# set1.intersection(set2)
# set1.symmetric_difference(set2)
# set1.symmetric_difference_update(set2)
# 
# set1.difference(set2)
# set1.difference_update(set2)
# 
# set1.isdisjoint(set2)
# set1.issubset(set2)
# set1.issuperset(set2)


# VERY IMPORTANT:
# An item, itself, inside a set, is UNMODIFIABLE. 
# Technically speaking, the item must be HASHABLE.
# Invalid set:  set(("book", [5,6], 7.8))  results in an error:
# TypeError: unhashable type: 'list'
# because [5,6] is a list, which is MODIFIABLE.

# VERY IMPORTANT:
# However, items can be removed from or added to the set.

 

set1 = {'cow', 'dog'}
set2 = {'pig', 'horse'}
# To combine sets, use set1.update(set2)
print("\nset1.update(set2) and set1.union(set2) will both")
print("add the elements from set2 to set1")
set1.update(set2)  # adds the elements in set2 to set1
print("\n", set1)

# Add an iterable, such as a list, tuple, dictionary, or string.
# This will add each item separately.
set1.update(['fox', 'mouse', 'deer'])
print(set1)

print("\nset1.update( string) will add each letter of the string one at a time")
set1.update("birthday")   # This will add each letter as separate elements
print("\n", set1)




print("\n\nWhat's the difference between set1.insection_update(set2) ")
print("and set1.intersection(set2)?")
print("\nThey both find the intersection of the 2 sets.")
print("However, in set1.intersection_update(set2), set1 is actually modified")
print("to hold the intersection.")
print("But in set1.intersection(set2), the intesection is returned ")
print("and set1 is not modified.")

print("\n\nset1.symmetric_difference(set2)")
print(" == the set of things that is NOT in BOTH sets.")
print("So it's the UNION of both sets - the INTERSECTION of both sets.")
print("\nset1.symmetric_difference(set2) will return the answer, w/out")
print("modifying set1 or set2.")
print("Use set1.symmetric_difference_update(set2) to put the answer ")
print("into the set1 variable.")


print("\n\nset1.difference(set2) ")
print("returns items that only exist in set1 and not set2")

print("\n\nset1.difference_update(set2) ")
print("removes items from set1 that are also in set2")

print("\n\nWhat's the difference between set1.difference_update(set2) ")
print("and set1.difference(set2)?")
print("\nThey both find the items that are in set1, but not set2.")
print("In set1.difference_update(set2), set1 is actually modified")
print("to hold the difference.")
print("But in set1.difference(set2), the difference is returned ")
print("and set1 is not modified.")


set1 = set([1,2,3,4])
set2 = set([2,4,6,8])
set3 = set([-4,-3,-2,-1])
set4 = set(range(8))

print(f"\n\nset1 = {set1}")
print(f"set2 = {set2}")
print(f"set3 = {set3}")

print("\nIs set1 and set2 disjoint?  (ie they have no intersection):")
print("set1.isdisjoint(set2)")
print(set1.isdisjoint(set2))

print("\nIs set1 and set3 disjoint?  (ie they have no intersection):")
print("set1.isdisjoint(set3)")
print(set1.isdisjoint(set3))

print("\nIs set1 a subset of set4?")
print("set1.issubset(set4)")
print(set1.issubset(set4))

print("\nIs set4 a superset of set1?")
print("set4.issuperset(set1)")
print(set4.issuperset(set1))
