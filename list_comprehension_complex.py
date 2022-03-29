# List comprehensions are usually faster than for loops.

###################################################
#
#  Filter a list using list comprehension
#
###################################################

lst = list(range(10))
print(f"Original list: {lst}")

# Keeps items that meet the condition x%3.
# So it keeps anything that has a remainder after dividing by 3.
# So it removes items that are divisible by 3.
lst2 = [x for x in lst if x%3]
print(lst2)

# Keeps items that meet the condition x>4
lst2 = [ x**2 for x in lst if x>4]
print(lst2)

# Filter a list using list comprehension with nested if statements.
# Keeps items that meet condition1 AND condition2.
# So it keeps items that are divisible by 2 and divisible by 3.
lst2 = [x for x in lst if x%2 == 0 if x%3 == 0]
print(lst2)



###################################################
#
#  List comprehension with...
#  No filter on the input list.
#  But modify the output, by using an if else statement.
#
###################################################

lst2 = ["Even" if x%2==0 else "Odd" for x in lst]
print(lst2)

lst2 = ["Odd" if x%2 else "Even" for x in lst]
print(lst2)



###################################################
#
#  Nested for loops within a list comprehension 
#
###################################################

# Generate every combo of first + last name
first_names = ["Alice", "Bernard", "Cecil", "Derrick", "Evan", "Fred"]
last_names = ["Smith", "Tanaka"]
name_generator = [ first + ' ' + last for first in first_names for last in last_names]
print(name_generator)



def transpose_matrix( matrix1):
    num_cols = len(matrix1[0])
    matrix2 = [[row[i] for row in matrix1] for i in range(num_cols)]
    print(matrix2)

def test_transpose_matrix():
    # These pairs of matricies are the transpose of the other.
    transpose_matrix( [[1,2,3,4]])
    transpose_matrix( [[1], [2], [3], [4]])

    transpose_matrix( [[1,2,3,4],[5,6,7,8]])
    transpose_matrix( [[1, 5], [2, 6], [3, 7], [4, 8]])

    transpose_matrix( [[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    transpose_matrix( [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]])

    transpose_matrix( [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    transpose_matrix( [[1, 5, 9, 13], [2, 6, 10, 14], 
                       [3, 7, 11, 15], [4, 8, 12, 16]])


test_transpose_matrix()


