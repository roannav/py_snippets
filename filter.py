# filter( filtering_function, lst)
# It will return a filter object, which keeps only the items in the list, 
# for which the filtering_function returns true.
# The second argument can be any iterable: list, tuple, dictionary

import random

# make a list of 10 numbers, which are random, and between 1-100
# random.randint():  both args are inclusive
lst = [ random.randint(1,100) for i in range(10)]
print(f"Original list: {lst}")


#filter() returns a filter object
odds_only_filter = filter(lambda x: (x%2 == 1) , lst)
print(odds_only_filter)
print(list(odds_only_filter))


greater_than_50_filter = filter(lambda x: x>50 , lst)
print(list(greater_than_50_filter))


# Is it greater than 10?  Returns True or False
def greater_than_10(x):
    return x>10

greater_than_10_filter = filter(greater_than_10, lst)
print(list(greater_than_10_filter))
print()


s = "Rosa Bonheur was a French artist known best as a painter of animals. She also made sculpture in a realist style."

words = s.split()
nums = list(range(len(words)))
print(words)
print(nums)

z = zip(nums, words)
print(z)  # zip object
d = dict(z)
print(d, '\n')

capital_words_filter = filter( lambda w: w.istitle() , words)
print(list(capital_words_filter))

# if we need to get the index too, we'll use the dictionary instead of the
# words list
capital_words_filter2 = filter( lambda item: item[1].istitle() , d.items())
print(list(capital_words_filter2))


