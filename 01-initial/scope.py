global_a = 3


def add(a, b):
    # global global_a
    # global_a = 4
    return a + b + global_a


from IPython import embed
embed()
