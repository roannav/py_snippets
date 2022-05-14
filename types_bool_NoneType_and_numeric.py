# This file covers 
# the boolean type: bool,  
# the none type: NoneType, 
# and the numberic types: int, float, and complex

import math

# <class 'bool'>
print(type(True))
print(type(False))

# <class 'NoneType'>
print(type(None))

# <class 'int'>
print(type(0))

# <class 'float'>
print(type(math.pi))

# scientific number    3 x 10**3
# Both e or E work the same.
f = 3e3   
print(f"3e3 = {f}")
print(type(f))

# <class 'complex'>
# complex number
# j is the imaginary part
i = 2+1j
print(f"2+1j = {i}")
print(type(i))

print(f"1j*1j = {1j*1j}")
print(type(1j*1j))
