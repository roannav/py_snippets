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
    

def run_tests():
    e1()
    e2()
    e3()
    e4()


run_tests()
