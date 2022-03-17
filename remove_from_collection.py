# What happens when you call remove() on each of the 4 different kinds of
# Python collections: list, tuple, dictionary, and set?

print("\ntldr: dictionary and tuple do NOT have a remove(item) method.")
print("For lists, use ValueError to catch removal of a non-existing item.")
print("For sets, use KeyError to catch removal of a non-existing item.")

import logging

# Try to remove the item "plum" from each of the collection types.

print("\nlist.remove(item) works")
lst = [ "plum", "peach", "pineapple" ]
lst.remove("plum")
print(lst)

try:
    print("\ntuple does not have a remove(item) method.")
    print("After all, tuples can't be modified.")
    tup = ( "plum", "peach", "pineapple" )
    tup.remove("plum")
except AttributeError as err: 
    logging.exception("")

try:
    print("\ndictionary does not have a remove(key) method.")
    print("Instead use dict.pop(key) or del dict[key]")
    d = { "plum":"purple", "peach":"orange", "pineapple":"yellow" }
    d.remove("plum")
except AttributeError as err: 
    logging.exception("")

print("\nset.remove(item) works")
set1 = { "plum", "peach", "pineapple" }
set1.remove("plum")
print(set1)



# What happens if you do the same tests but try to remove a non-existing item?

# Try to remove the item "foo" from each of the collection types.


try:
    print("\nlist.remove(item) works, but need to catch ValueError")
    print("for items that don't exist in the list")
    lst = [ "plum", "peach", "pineapple" ]
    lst.remove("foo")
    print(lst)
except ValueError as err:
    logging.exception("")


try:
    print("\ntuple does not have a remove(item) method.")
    print("After all, tuples can't be modified.")
    tup = ( "plum", "peach", "pineapple" )
    tup.remove("foo")
except AttributeError as err: 
    logging.exception("")

try:
    print("\ndictionary does not have a remove(key) method.")
    print("Instead use dict.pop(key) or del dict[key]")
    d = { "plum":"purple", "peach":"orange", "pineapple":"yellow" }
    d.remove("foo")
except AttributeError as err: 
    logging.exception("")

try:
    print("\nset.remove(item) works, but need to catch KeyError")
    print("for items that don't exist in the set")
    set1 = { "plum", "peach", "pineapple" }
    set1.remove("foo")
    print(set1)
except KeyError as err: 
    logging.exception("")


