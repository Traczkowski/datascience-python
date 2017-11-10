import random
from classification import classify
from etl import read_iris_file


def examples_split(examples, ratio):
    """
    From a list of examples,
    "splits" it into two sublists according to ratio.

    Parameters
    ----------
    example_a : one {tuple} formated like (5.1, 3.5, 1.4, 0.2, 'setosa')
    example_b : another {tuple} formated like (5.1, 3.5, 1.4, 0.2, 'setosa')

    Returns
    -------
    train: {list} of {tuple}
    test: {list} of {tuple}

    Example
    -------
    >>> examples = read_iris_file("iris.csv")
    >>> train, test = examples_split(examples, 0.7)
    >>> (len(train)+len(test)) == len(examples)
    True
    """
    cutoff = round(len(examples) * ratio)
    random.shuffle(examples)
    return examples[:cutoff], examples[cutoff:]


def compute_score(train, test):
    """
    From each simple example_x taken in test,
    obtains a classification using train as examples for classify()
    Checks if classify finds the correct class.
    Returns the proportion of successful classifications.

    Parameters
    ----------
    train: {list} of {tuple}
    test: {list} of {tuple}

    Returns
    -------
    {float} : the proportion of successful classifications in test using train
    """
    return sum([classify(sample, train) == sample[4] for sample in test]) / len(test)


if __name__ == '__main__':
    examples = read_iris_file("iris.csv")
    print("loaded {} examples from 'iris.csv'".format(len(examples)))

    train, test = examples_split(examples, 0.7)

    print("train contains now {} examples".format(len(train)))
    print("test contains now {} examples".format(len(test)))

    print("score obtained: {}".format(compute_score(train, test)))
