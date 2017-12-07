import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def __str__(self):
        return "{} sided".format(self.sides)

    def __repr__(self):
        return self.__str__()

    def roll(self, attempts):
        return [random.randint(1, self.sides) for _ in range(attempts)]


class Experiment:
    def __init__(self, sides, attempts, samples):
        self.sides = sides
        self.attempts = attempts
        self.samples = samples
        self.get_samples()
        self.get_sample_means()
        self.get_overall_mean()

    def get_samples(self):
        die = Die(self.sides)
        self.sample_rolls = [die.roll(self.attempts)
                             for _ in range(self.samples)]

    def get_sample_means(self):
        self.sample_means = [sum(s) / len(s) for s in self.sample_rolls]

    def get_overall_mean(self):
        self.mean = sum(self.sample_means) / self.samples


e = Experiment(6, 5, 1000)
