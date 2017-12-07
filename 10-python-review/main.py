def mean(numbers):
    return sum(numbers) / len(numbers)


def root(number):
    return number ** 0.5


expenses = {}
with open('expense.txt') as f:
    for line in f:
        name, amt = line.strip().split(',')
        print('name:', name, 'amt:', amt)
        if name not in expenses:
            expenses[name] = []
        expenses[name].append(float(amt))
