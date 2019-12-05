import sys
import re

originalList = [17, 38, 10, 25, 72]


def function1(list):
    """
    Sort the list.

    :param list:
    :type list: array[int]
    :return: list
    :rtype: array[int]
    """
    list.sort()
    return list


def function2(list):
    """
    Append 12 at the end of the list.

    :param list:
    :type list: array[int]
    :return: list
    :rtype: array[int]
    """
    list.append(12)
    return list


def function3(list):
    """
    Reverse the list.

    :param list:
    :type list: array[int]
    :return: list
    :rtype: array[int]
    """
    list.reverse()
    return list


def function4(list):
    """
    Search and return the index of 17 in the list.

    :param list:
    :type list: array[int]
    :return: list
    :rtype: array[int]
    """
    return list.index(17)


def function5(list):
    """
    Remove value 38 of the list.

    :param list:
    :type list: array[int]
    :return: list
    :rtype: array[int]
    """
    list.remove(38)
    return list


def function6(list):
    """
    Return the list from element 1 to 3.

    :param list:
    :type list: array[int]
    :return: list
    :rtype: array[int]
    """
    return list[1:3]


def function7(list):
    """
    Return the list until element 2.

    :param list:
    :type list: array[int]
    :return: list
    :rtype: array[int]
    """
    return list[:2]


def function8(list):
    """
    Return the list from element 2.

    :param list:
    :type list: array[int]
    :return: list
    :rtype: array[int]
    """
    return list[2:]


def function9(list):
    """
    Return the list.

    :param list:
    :type list: array[int]
    :return: list
    :rtype: array[int]
    """
    return list


def function10(list):
    """
    Return the last element of the list.

    :param list:
    :type list: array[int]
    :return: list
    :rtype: array[int]
    """
    return list[-1]


if __name__ == "__main__":
    print(function1(originalList.copy()))
    print(function2(originalList.copy()))
    print(function3(originalList.copy()))
    print(function4(originalList.copy()))
    print(function5(originalList.copy()))
    print(function6(originalList.copy()))
    print(function7(originalList.copy()))
    print(function8(originalList.copy()))
    print(function9(originalList.copy()))
    print(function10(originalList.copy()))
