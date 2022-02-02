# VERY IMPORTANT:   before MODIFYING a global variable in a function,
# you must add this line to the TOP of the function:
# global <var_name>
#
# Otherwise, without global <var_name> at the top of the function,
# an assignment like <var_name> = 1 would be CREATING A LOCAL VAR.

def foo():
    global x
    x = 1

x = 2
foo()
print(x)    # Output: 1


#----------------------------------------------------------------------
def foo2():
    #global x

    # Because no global statement above,
    # a local variable x is created.
    x = 1

x = 2
foo2()
print(x)    # Output: 2

