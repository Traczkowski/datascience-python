from etl import read_iris_file
from collections import Counter


def distance(example_a, example_b):
    """
    From a list of examples of iris,
    returns the most common class of iris occuring in there.

    Parameters
    ----------
    example_a : one {tuple} formated like (5.1, 3.5, 1.4, 0.2, 'setosa')
    example_b : another {tuple} formated like (5.1, 3.5, 1.4, 0.2, 'setosa')

    Returns
    -------
    {float} : the distance considering 4 first coordinates

    Example
    -------
    >>> round( distance((1.0,0.0,0.0,0.0,'setosa'), (0.0,0.0,1.0,0.0,'setosa')), 6)
    1.414214
    >>> round( distance((1.0,0.0,3.0,0.0,'setosa'), (4.0,0.0,7.0,0.0,'setosa')), 6)
    5.0
    """
    return sum([(example_a[i] - example_b[i]) ** 2 for i in range(4)]) ** 0.5


def closest(example_x, examples):
    """
    Returns the one example from a list of examples that is
    the closest to a given example_x using distance()

    Parameters
    ----------
    example_x : one {tuple} formated like (5.1, 3.5, 1.4, 0.2, 'setosa')
    examples : a {list} of {tuple} each formated like (5.1, 3.5, 1.4, 0.2, 'setosa')

    Returns
    -------
    {tuple} : the closest one

    Example
    -------
    >>> examples = [ (1.0, 0.0, 0.0, 0.0, 'setosa'), (0.0, 2.0, 0.0, 0.0, 'virginica'), (0.0, 0.0, 3.0, 0.0, 'versicolor') ]
    >>> closest( (2.0, 0.0, 0.0, 0.0, None), examples )
    (1.0, 0.0, 0.0, 0.0, 'setosa')
    >>> closest( (0.0, 1.0, 0.0, 0.0, None), examples )
    (0.0, 2.0, 0.0, 0.0, 'virginica')
    >>> closest( (2.0, 0.0, 4.0, 0.0, None), examples )
    (0.0, 0.0, 3.0, 0.0, 'versicolor')
    """
    length, sample = distance(example_x, examples[0]), examples[0]
    for i in range(1, len(examples)):
        tmplen = distance(example_x, examples[i])
        if tmplen < length:
            length, sample = tmplen, examples[i]
    return sample


def classify(example_x, examples):
    """
    For a given example_x, finds the closest example in a list of examples.
    Returns the class of that closest example.

    Parameters
    ----------
    example_x : one {tuple} formated like (5.1, 3.5, 1.4, 0.2, 'setosa')
    examples : a {list} of {tuple} each formated like (5.1, 3.5, 1.4, 0.2, 'setosa')

    Returns
    -------
    {str} : the label of the closest one

    Example
    -------
    >>> examples = [ (1.0, 0.0, 0.0, 0.0, 'setosa'), (0.0, 2.0, 0.0, 0.0, 'virginica'), (0.0, 0.0, 3.0, 0.0, 'versicolor') ]
    >>> classify( (2.0, 0.0, 0.0, 0.0, None), examples )
    'setosa'
    >>> classify( (0.0, 1.0, 0.0, 0.0, None), examples )
    'virginica'
    >>> classify( (2.0, 0.0, 4.0, 0.0, None), examples )
    'versicolor'
    """
    return closest(example_x, examples)[-1]


if __name__ == '__main__':
    examples = read_iris_file("iris.csv")

    example_x = (5.1, 3.5, 1.4, 0.2, None)
    print("example_x == {}".format(example_x))
    print("closest to x in examples == {}".format(closest(example_x, examples)))
    print("classified as: {}".format(classify(example_x, examples)))
    print("(it was supposed to be 'setosa')")
    print()

    example_x = (6.5, 2.8, 4.6, 1.5, None)
    print("example_x == {}".format(example_x))
    print("closest to x in examples == {}".format(closest(example_x, examples)))
    print("classified as: {}".format(classify(example_x, examples)))
    print("(it was supposed to be 'versicolor')")
    print()

    example_x = (6.4, 2.8, 5.6, 2.1, None)
    print("example_x == {}".format(example_x))
    print("closest to x in examples == {}".format(closest(example_x, examples)))
    print("classified as: {}".format(classify(example_x, examples)))
    print("(it was supposed to be 'virginica')")
