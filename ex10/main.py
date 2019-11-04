def main(liste):
    """
    Return list

    @return ret
    @rtype array[int]
    """
    ret = [x+3 if x > 2 else x for x in liste]
    return ret


if __name__ == "__main__":
    res = main([n for n in range(6)])
    print(str(res))
