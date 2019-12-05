def main(str1, str2):
    """
    Return list

    :param str1:
    :type str1: str
    :param str2:
    :type str2: str
    :return: ret
    :rtype: array[int]
    """

    ret = [x + y for x in str1 for y in str2]
    return ret


if __name__ == "__main__":
    res = main("abc", "de")
    print(str(res))
