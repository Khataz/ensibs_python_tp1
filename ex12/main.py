import sys
import re

X = {'a', 'b', 'c', 'd'}
Y = {'s', 'b', 'd'}

def function1():
    return X, Y

def function2():
    return 'c' in X

def function3():
    return 'a' in Y

def function4():
    return X-Y

def function5():
    return Y-X

def function6():
    return X|Y

def function7():
    return X&Y

if __name__ == "__main__":
    print(function1())
    print(function2())
    print(function3())
    print(function4())
    print(function5())
    print(function6())
    print(function7())