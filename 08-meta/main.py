class Dog:
    def __init__(self, name):
        self.name = name

    def __dir__(self):
        return [1, 2, 3]

    def __getattribute__(self, name):
        # always called when getting an attribute
        print('calling getattribute', name)
        return object.__getattribute__(self, name)

    def __getattr__(self, name):
        # only gets called if attribute is NOT found
        print('calling getattr:', name)
        return "lol"

    def __setattr__(self, name, value):
        # always called when setting an attribute
        print('calling setattr:', name, 'value:', value)
        object.__setattr__(self, name, value)


d = Dog('fido')
