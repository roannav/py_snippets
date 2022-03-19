import math

# Use lambda function as an anonymous function inside another function.
# The containing function is called a higher-order function.

# A higher-order function will either
#   1) return a function
#   2) take an argument that is a function

def multiplier(k):
    return lambda x: x*k

def test_multiplier():
    double = multiplier(2)
    triple = multiplier(3)

    print(double(2))
    print(triple(2))

test_multiplier()


def word_modifier(word_beginning='', word_ending=''):
    return lambda word: word_beginning + word + word_ending

def test_multiplier():
    add_ing = word_modifier('', 'ing')

    print(add_ing("row"))
    print(add_ing("read"))

    prepend_non = word_modifier('non', '')

    print(prepend_non("verbal"))
    print(prepend_non("toxic"))

test_multiplier()


def calculate( x, rounding_function):
    answer = rounding_function(x)
    return answer

def test_calculate():
    print(calculate( 1.87, math.floor))
    print(calculate( 1.87, math.ceil))

test_calculate()
