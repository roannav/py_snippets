# 3 Ways to get the key of the dictionary, when you know the value

d = { 1: "one", 
      2: "two",
      3: "three",
      4: "four"
}
print(d, '\n')


# Method #1
# NOTE: get the key of the dictionary, when you know the value
# index = list(d.values()).index(value)
# key = list(d.keys())[index]
index = list(d.values()).index('two')
key = list(d.keys())[index]
print(key)


# Method #2
# NOTE: get the key of the dictionary, when you know the value
def get_key(d, val):
    for k,v in d.items():
        if v == val:
            return k
    return None

key = get_key(d, "three")
print(key)


# Method #3
# NOTE: get the key of the dictionary, when you know the value
key = [k for k,v in d.items() if v=="one"][0]
print(key)


