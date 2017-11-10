import random


def f1(x): return x ** 2


def f2(x): return x ** 0.5


def f3(x): return x + random.random()


fns = [f1, f2, f3]
ans = {i: f(i + 3) for i, f in enumerate(fns)}
print(ans)
