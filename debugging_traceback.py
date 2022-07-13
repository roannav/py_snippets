import traceback

# In the code below,
# since every Exception is handled with a try-except statement,
# it doesn't cause an automatic printout of a traceback.

# But we can force the traceback to be printed
# via traceback.format_exc()
try:
    raise Exception("Opps")
except:
    print(traceback.format_exc())



def goo():
    raise Exception("goo(): Opps")

def foo():
    goo()

try:
    foo()
except:
    print(traceback.format_exc())



try:
    foo()
except:
    err_filename = 'debugging_traceback.txt'
    err_file = open(err_filename, 'w')
    err_file.write(traceback.format_exc())
    err_file.close()
