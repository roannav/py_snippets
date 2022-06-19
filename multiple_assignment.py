# f-string {var=} requires Python 3.8
# eg print(f"{i=}  {j=}")

i = j = 2
print(f"i={i:<10}j={j}")

i, j = 3, 4
print(f"i={i:<10}j={j}")

# swap the values of 2 variables
i, j = j, i
print(f"i={i:<10}j={j}")

# assign a list to i
*i, j = 5, 6, 7
print(f"i={i}    j={j}")

# assign a list to j
i, *j = 8, 9, 10    # can be just numbers
print(f"i={i:<10}j={j}")

i, j = (11, 12)     # can be a tuple
print(f"i={i:<10}j={j}")

i, j = [13, 14]     # can be a list
print(f"i={i:<10}j={j}")


# First step:  a, c, and d are assigned.
# Then the remaining numbers are assigned as a LIST to b.
a, *b, c, d = range(10)
print(f"a={a:<10}b={b}  c={c:<10}d={d:<10}")
