# you can test this by typing:
# python -m doctest etl.py

# or just try to execute it:
# python etl.py


def read_iris_line(line):
    """
    Parses a line from the iris dataset and returns
    the corresponding tuple

    Parameters
    ----------
    line   : {str}

    Returns
    -------
    tuple

    Example
    -------
    >>> read_iris_line("5.1,3.5,1.4,0.2,setosa")
    (5.1, 3.5, 1.4, 0.2, 'setosa')
    >>> read_iris_line("5.9,3,5.1,1.8,virginica")
    (5.9, 3.0, 5.1, 1.8, 'virginica')
    """
    return tuple(float(x) if i < 4 else x for i, x in enumerate(line.split(',')))


def read_iris_file(filepath):
    """
    Parses the iris csv file and returns a list of tuples.
    Discards whatever is on the first line (headers).

    Parameters
    ----------
    filepath : {str} providing the path to the file

    Returns
    -------
    list of tuples

    Example
    -------
    >>> read_iris_file("iris.csv")[0]
    (5.1, 3.5, 1.4, 0.2, 'setosa')
    >>> read_iris_file("iris.csv")[-1]
    (5.9, 3.0, 5.1, 1.8, 'virginica')
    """
    tuples = []
    with open(filepath) as f:
        for i, line in enumerate(f):
            if i > 0:
                tuples.append(read_iris_line(line.strip()))
    return tuples


if __name__ == '__main__':
    print("*** parsing one line...")
    example_line = "5.1,3,1.4,0.2,setosa"
    example_tuple = read_iris_line(example_line)

    # showing the result
    print("value returned: {}".format(example_tuple))

    # checking types found within one example
    print("value returned is a tuple: {}".format(
        isinstance(example_tuple, tuple)))

    print("value returned has len 5: {}".format(len(example_tuple) == 5))

    for i in range(4):
        print("type on index {} is float: {}".format(
            i, isinstance(example_tuple[i], float)))
    print("type on index {} is str: {}".format(
        4, isinstance(example_tuple[4], str)))
    print()

    print("*** reading 'iris.csv'...")
    # should just not make any error ;)
    examples = read_iris_file("iris.csv")

    # should be 150
    print("there are {} examples in 'iris.csv'".format(len(examples)))

    # should be 5 exactly (between 5 and 5)
    print("examples length is between {} and {}".format(max(map(len, examples)),
                                                        min(map(len, examples))))
    print()
