"""
The Module Docstring
"""


class Dog:
    """
    The Dog blueprint
    """
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__private = 'shhhh'
        self._notprivate = 'public'
        Dog.counter += 1

    def __repr__(self):
        return "{0} is {1} years old".format(self.name, self.age)

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        return [self, other]

    def __del__(self):
        """
        runs when self gets deleted
        """
        pass

    def speak(self):
        """
        Speak method
        """
        return "{0} says woof!".format(self.name)
