from newmath import *

c = add(3, 4)
d = sub(6, 7)


def stuff(*nums, **kwargs):
    print(kwargs)
    return sum(nums)
    # s = 0
    # for n in nums:
    #     s += n
    # return s


print(stuff(2, 3, 4, name='sum', age=3))


def more(a, b=1, c=2):
    return a * b * c


more(3, c=9, b=7)
