def main():
    """
    Return integers form 0 to 15 (not inclued), with a step of 3.

    @return ret
    @rtype array[int]
    """
    ret = []
    for i in range(0, 15, 3):
        ret.append(i)
    return ret


if __name__ == "__main__":
    res = main()
    for e in res:
        print(str(e))
