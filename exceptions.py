import logging

def e1():
    try:
        li = [ 2 ]
        print(li[9])
    except IndexError as e:
        print("IndexError")
        print(e)
    else:
        print("No exception.")
    finally:
        print("Finally is always done.\n")


def e2():
    try:
        with open('does_not_exist.txt') as f:
            txt = f.read()
    except FileNotFoundError as e:
        print("FileNotFoundError")
        print(e)
    else:
        print("The file contents are")
        print(txt)
    finally:
        print("Try-except is done... finally.\n")


def e3():
    try:
        with open('exceptions.py') as f:
            txt = f.read()
    except FileNotFoundError as e:
        print("FileNotFoundError")
        print(e)
    else:
        print("The first part of the file contents are")
        print(txt[:30])
        print(type(txt))
    finally:
        print("Try-except is done... finally.\n")


def e4():
    try:
        lala = 1/0
    except Exception as ex:
        # STUDY:  This an anti-pattern and can hide unexpected errors.
        # If we must use a non-specific Exception block to catch all Exceptions,
        # then we must print a stack trace.
        logging.exception("Exception")
        print(ex)
    

def e5():
    try:
        lala = 1/0
    except ZeroDivisionError as ex:
        print("\nZeroDivisionError")
        print(ex)


def e6():
    try:
        print(foo)
    except NameError as e:
        print("\nNameError")
        print(e)


def e7():
    try:
        d = {"Mary": "Black", "Suzy": "Orange", "Tammy": "Green"}
        print(d["Zoe"])
    except KeyError as e:
        print("\nKeyError")
        print(e)
        print()


def e8():
    d = {"Mary": "Black", "Suzy": "Orange", "Tammy": "Green"}
    print(d["Zoe"])
    # When this crashes the program, it will print a stack trace,
    # whereas catching the error in an except block,
    # will not automatically print a stack trace.


def e9():
    try:
        assert False, "e9(): assertion fails"
    except AssertionError as e:
        print("\nAssertionError")
        print(e)
    else:
        print("No error occurred.")
    finally:
        print("Done with e9()")



def run_tests():
    '''
    e1()
    e2()
    e3()
    e4()
    e5()
    '''
    e6()
    e7()
    #e8()
    e9()

run_tests()
