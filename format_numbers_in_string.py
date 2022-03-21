import math

# Round a float to some degree of precision, within a string.
# Right AFTER the ., put the number of decimal places you want.
# Then append an 'f' to signify that it is a float.

# The number AFTER the : (and BEFORE the '.' if it exists), is the 
# width (how many columns) the number will be printed in

# Python 3.8 has the = shortcut in f-strings
# eg  x=2;  print(f'{x=}')  
# ===> x=2

print(f"math.pi:1.4f = {math.pi:1.4f}")
print("===>  3.1416   (so it rounds up!)")

print(f"\nmath.pi:2.4f = {math.pi:2.4f}")
print(f"math.pi:3.4f = {math.pi:3.4f}")
print(f"math.pi:4.4f = {math.pi:4.4f}")
print(f"math.pi:5.4f = {math.pi:5.4f}")
print(f"math.pi:6.4f = {math.pi:6.4f}")
print(f"math.pi:7.4f = {math.pi:7.4f}")
print(f"math.pi:8.4f = {math.pi:8.4f}")


print("\nold way: 'The result is {r:1.2f}'.format(r = 3.141592)")
print('The result is {r:1.2f}\n'.format(r = 3.141592))

for i in range(10):
    print(f"math.e:1.{i}f = {math.e:1.{i}f}")

print("\n\n\n                              123456789012345678901234567890")
for i in range(1,12):
    print(f"{10**i * math.e : 15} : 25.{i:<2}f = {math.pow(10,i) * math.e : 25.{i}f}")
print("\nThe number after the ':' indicates the width of the entire number")
print("(integer and decimal parts).  In this case, it's 25 char width.")

nums = [1, 81, 625, 2401, 14641, 207361, 2856178, 38413576]

print("\n\n\nnums is", nums, "\n")

print("{i:10}      {i:<10}    {i:^10}")
for i in nums:
    print(f"{i:10}  {i:<10}{i:^10}")
print("\n< means to justify the number to the left.")
print("\n> means to justify the number to the right.")
print("\n^ means to center-justify the number.")


print("\n\n\n{i:010}     {i:<10}    {i:^10}")
for i in nums:
    print(f"{i:010}  {i:<10}{i:^10}")
print("\nThe added '0' just after the ':' means...")
print("if the number is shorter than the 10 char width,")
print("then prefix it with 0's")
