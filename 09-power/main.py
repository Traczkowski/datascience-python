import random

expenses = {}
with open('expense.txt') as f:
    for line in f:
        name, amt = line.strip().split(',')
        if name not in expenses:
            expenses[name] = []
        expenses[name].append(float(amt))


class Die:
    def __init__(self, rolls):
        self.rolls = rolls

    def roll(self):
        return [random.randint(1, 6) for _ in range(self.rolls)]


class Experiment:
    def __init__(self, n, rolls):
        self.n = n
        self.rolls = rolls
        self.get_samples()
        self.compute_sample_means()
        self.compute_mean()

    def get_samples(self):
        d = Die(self.rolls)
        self.samples = [d.roll() for _ in range(self.n)]

    def compute_sample_means(self):
        self.sample_means = list(map(lambda s: sum(s) / len(s), self.samples))

    def compute_mean(self):
        self.mean = sum(self.sample_means) / len(self.sample_means)


e = Experiment(50, 6)
