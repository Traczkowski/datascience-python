def addone(f):
    # packing (tuple, dict)
    def inner(*args, **kwargs):
        # unpacking
        return f(*args, **kwargs) + 1
    return inner


@addone
def square(x):
    return x ** 2


@addone
def area(l, w):
    return l * w


print('3 squared + 1 =', square(3))
print('area 3x7 + 1 =', area(3, w=7))
