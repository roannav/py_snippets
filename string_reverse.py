import logging

s = "happy birthday"
print(f"Original string: {s}")

# print string in reverse order
print(s[::-1])

# print string in reverse order, taking steps of 2 at a time.
# So in other words, it is printing every 2nd letter,
# but starting from the end, and heading to the beginning
# of the string.
print(s[::-2])


print("\nReverse a string with reversed(str).")
print("This does NOT change the original string.")
s = 'Happy New Year'
print(''.join(reversed(s)))
print()


# Lists, but NOT strings, have a reverse() method.
try:
    s.reverse()
except AttributeError as err:
    logging.exception("Strings don't have a reverse() method")


