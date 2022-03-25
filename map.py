# map( function, iterable)
# To each item in the iterable, apply the function

def square(x):
    return x**2

print(list(map(square, list(range(5)))))

print(list(map(lambda x: x*x, list(range(5)))))


def get_len(x):
    return len(x)

print(list(map(get_len, ['hat', 'shirt', 'scarf'])))

print(list(map(len, ['hat', 'shirt', 'scarf'])))

