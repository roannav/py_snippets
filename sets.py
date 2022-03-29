import logging

# sets are a kind of collection.
# Python has 4 built-in collection types: list, tuple, dictionary and set.
# Unlike the other collections, sets have no order, so you can't index 
# into them.  (Dictionaries used to have no order, but now they do.)
# Like mathematical sets, you can not repeat an item, so in other words,
# each item in a set must be unique.
# Also like math sets, the curly braces { } are used to hold all the items.

# VERY IMPORTANT:
# An item, itself, inside a set, is UNMODIFIABLE. 
# Technically speaking, the item must be HASHABLE.
# Invalid set:  set(("book", [5,6], 7.8))  results in an error:
# TypeError: unhashable type: 'list'
# because [5,6] is a list, which is MODIFIABLE.

# VERY IMPORTANT:
# However, items can be removed from or added to the set.

print("\nThe set() constructor takes only 1 (or 0) arguments.")
print("So this would cause TypeError: set expected at most 1 arguments, got 3:")
print("set1 = set(1, 2, 3)")

print("\nThe set() constructor can take an iterable, such as a list, " + \
      "tuple, or string.")
print("\nThese are all valid ways to create a set:")

print("\nset2 = set(('book', (5,6), 7.8))")
set2 = set(("book", (5,6), 7.8))
print(set2)

print("\nset3 = set(['cup', 'water'])")
set3 = set(['cup', 'water'])
print(set3)

print("\nset4 = set('world')")
set4 = set("world")
print(set4)

# Tip:
# When you create a set, it will automatically remove the duplicates for you.
set5 = { 1, 1, 1, 2, 3}
print(f"\n{set5}\n")

# Tip: don't create an empty set like this...
#set6 = {}  # This is actually an empty DICTIONARY

# Instead make an empty set with the set() constructor
set7 = set()
print(f"Empty set created with set() constructor: {set7}")


# TODO: What happens to the True, in case #1?
# set1 = { 1, True, "hi", False }  --> { 1, "hi", False }
# set1 = { 2, True, "hi", False }  --> { 2, True, "hi", False }
set1 = { 1, True, "hi", False }
print(f"\nset1 is {set1}")


print("\nIs 'Wally' in set1?")
if "Wally" in set1:
    print("Found Wally")
elif "Wally" not in set1:
    print("Wally was not found")

# To add a single item to a set
print("\nset1.add(item)  adds a ONLY a SINGLE ITEM to the set")
set1.add(None)
print(set1)

# NOTE: (1,2) is a single item.  This will add the tuple to the set.
# It will not add 2 items separately.
print("\nadd a tuple (1,2)  to the set")
set1.add((1,2))
print(set1)

# To combine sets, use set1.update(set2)
print("\nset1.update(set2) and set1.union(set2) will both")
print("add the elements, one by one, from set2 to set1.\n")
set1.update(set2)  # adds the elements in set2 to set
print(set1)

# Add an iterable, such as a list, tuple, dictionary, or string.
# This will add each item separately.
set1.update(['fox', 'mouse', 'deer'])
print(set1)

set1.update("birthday")   # This will add each letter as separate elements
print(set1)


print(f"\nLength of the set is {len(set1)}")
print(f"Data type of set is {type(set1)}")

if 'fox' in set1:
    print("\nCalling set1.remove('fox')")
    set1.remove('fox')
    print(set1)
    print(f"Length of the set is {len(set1)}")

try:
    print("\nTrying to remove element 'ocean'")
    set1.remove('ocean')   # 'ocean' is already not in the set
    print(set1)
    print(f"Length of the set is {len(set1)}")
except KeyError as err:
    print("set.remove(element) will cause a KeyError, " + \
          "if the element is not in the set.\n")
    logging.exception(err)


print("\nTrying to remove element 'ocean' again.")
print("set.discard(element) fails silently if the element is not in the set.\n")
set1.discard('ocean')   # 'ocean' is already not in the set
print(set1)
print(f"Length of the set is {len(set1)}")


print("\nset.pop() removes the last element.  However, since a " + \
      "set is unordered,")
print("set.pop(), in essence, RANDOMLY removes an element.\n")
set1.pop()
print(set1)
print(f"Length of the set is {len(set1)}")

set2 = set1.copy()

print("\nset.clear()")
set1.clear()
print(set1)
print(f"Length of the set is {len(set1)}")

print("\nSetting set back to an old copy of itself")
set1 = set2.copy()
print(set1)
print(f"Length of the set is {len(set1)}")

try:
    print("\nCalling del set1")
    del set1     # so the variable set will no longer exist
    print(set1)  # generates NameError: name 'set' is not defined
except NameError as err:
    print("del set1 ==> means set1 no longer exists.")
    print("So an error is generated if we try to use that variable.\n")
    logging.exception(err)
else:
    print("no exception")
finally:
    print("\nDone with del set1")

