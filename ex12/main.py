X = {'a', 'b', 'c', 'd'}
Y = {'s', 'b', 'd'}


def function1():
    return X, Y


def function2():
    return 'c' in X


def function3():
    return 'a' in Y


def function4():
    return X - Y


def function5():
    return Y - X


def function6():
    return X | Y


def function7():
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
