import random


class Dog:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.weight = 1
        self.sex = random.choice(['m', 'f'])

    def __str__(self):
        return "{} is {} years old and is {} and weighs {} lbs".format(self.name, self.age, self.sex, self.weight)

    def __repr__(self):
        return self.__str__()

    def bark(self):
        return "Woof! My name is {}".format(self.name)

    def feed(self, weight):
        self.weight += weight


d1 = Dog('fido')
d2 = Dog('lassy')
d3 = Dog('molly')
d1.feed(3)
d1.feed(3)
d1.feed(3)
d1.feed(3)
dogs = [d1, d2, d3]
