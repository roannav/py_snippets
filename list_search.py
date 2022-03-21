import logging

# NOTE: Both lists and strings have an index(item) method, which acts the 
#       same way.
# NOTE: However, lists do not have a find(item) method; only strings do.

lst = ['red', 'orange', 'yellow']

#print(lst.index['yellow'])
#==> TypeError: 'builtin_function_or_method' object is not subscriptable

print(lst.index('yellow'))

try:
    print(lst.index('green'))
except ValueError as err:
    logging.exception("")


