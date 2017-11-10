def add(a, b):
    """
    Adds two numbers
    """
    return a + b


def sub(a, b):
    return a - b


def euclidean_distance(vector):
    """
    Computes the L2 norm/Euclidean distance
    tuple -> float
    """
    return sum([d ** 2 for d in vector]) ** 0.5


def unit_vector(vector):
    """
    Compute the unit vector. Make length 1.
    tuple -> tuple
    """
    l2 = euclidean_distance(vector)
    return tuple(d / l2 for d in vector)
