mod2 = lambda num: num % 2

print(mod2(5))

################################################################

# def() vs. lambda()

def square(n):
    return n*n

lambda_square = lambda n: n*n

# NOTE: A regular function always returns something, 
# even if it's an implicit None.
# A lambda function does not use a 'return' keyword.
# Instead, the expression after the :, is returned.
# A lambda definition is a function and can be assigned to a variable.
# And then you can call the function through that assigned variable.
# Use a lambda function in place of an ordinary function.

print(square(7))
print(lambda_square(7))
(lambda n: print(n*n))(7)


################################################################

def add2(x):
    return x + 2

lambda_add2 = lambda x: x + 2

print(add2(6))
print(lambda_add2(6))
print((lambda x: x + 2)(6))

################################################################

def isOdd(x):
    return (x%2 == 1)

lambda_isOdd = lambda x: x%2 == 1

print(isOdd(3))
print(lambda_isOdd(3))
print((lambda x: x%2 == 1)(3))

################################################################

def addUp( a, b, c):
    return a + b + c

lambda_addUp = lambda a, b, c: a + b + c

print(addUp(4,6,7))
print(lambda_addUp(4,6,7))
print((lambda a,b,c: a+b+c)(4,6,7))

################################################################

# Here, the lambda function has not been called.  It is only defined.
# So it will print the function object and its memory location.
# Result:  <function <lambda> at 0x7fb30485a9e0>
print(lambda x : x)

# This is the way to pass an argument to the anonymous function
print((lambda x : x)("hey"))

################################################################
x ="macromolecules"

# The argument x is passed through the lambda function, and then printed
(lambda x : print(x))(x)

