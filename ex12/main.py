X = {'a', 'b', 'c', 'd'}
Y = {'s', 'b', 'd'}


def function1():
    """
    Return X,Y.

    :param none:
    :return: X, Y
    :rtype: set
    """
    return X, Y


def function2():
    """
    Return if c is in X.

    :param none:
    :return: 'c' in X
    :rtype: boolean
    """
    return 'c' in X


def function3():
    """
    Return if a is in Y.

    :param none:
    :return: 'a' in Y
    :rtype: boolean
    """
    return 'a' in Y


def function4():
    """
    Return X - Y.

    :param none:
    :return: X - Y
    :rtype: set
    """
    return X - Y


def function5():
    """
    Return Y - X.

    :param none:
    :return: Y - X
    :rtype: set
    """
    return Y - X


def function6():
    """
    Return X union Y.

    :param none:
    :return: X union Y
    :rtype: set
    """
    return X | Y


def function7():
    """
    Return X inter Y.

    :param none:
    :return: X inter Y
    :rtype: set
    """
    return X & Y


if __name__ == "__main__":
    print("X :", function1()[0])
    print("Y :", function1()[1])
    print("c in X :", function2())
    print("a in Y :", function3())
    print("X - Y :", function4())
    print("Y - X :", function5())
    print("X union Y :", function6())
    print("X inter Y :", function7())
