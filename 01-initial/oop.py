class Cat:
    count = 3

    def add():
        Cat.count += 1

    def __init__(self, name):
        self.name = name

    def meow(self):
        return "{} says hello".format(self.name)

    def lol(haz):
        return haz.name


# ---------------
c = Cat('mews')
# ---------------


def sample(*args, **kwargs):
    print('args:', args, 'kwargs:', kwargs)
