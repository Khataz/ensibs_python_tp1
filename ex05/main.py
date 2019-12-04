def main():
    """
    Return integers form 0 to 15 (not inclued), with a step of 3.

    :param None:
    :return ret: [0, 3, 6, 9, 12]
    :rtype: array[int]
    """
    ret = []
    for i in range(0, 15, 3):
        ret.append(i)
    return ret


if __name__ == "__main__":
    res = main()
    print(res)
