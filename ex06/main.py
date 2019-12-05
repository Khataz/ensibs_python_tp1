import sys
import re
import numpy as np


def cube(value):
    """
    Return the cube of value.

    :param value: line in input, format : FLOAT<pression>;FLOAT<volume>
    :type value: float
    :return: value**3
    :rtype: float
    """
    return value**3


def volumeSphere(r):
    """
    Return the volume of a sphere of radius r.

    :param r: raise
    :type r: float
    :return: 4 / 3 * np.pi * cube(r)
    :rtype: float
    """
    return 4 / 3 * np.pi * cube(r)


def main(line):
    """
    Return the volume of a sphere of the specified radius.

    :param line: line in input, format : FLOAT<rayon>
    :type line: string
    :raises Exception: 100 - BAD INPUT: Not a positive number
    :raises Exception: 200 - BAD INPUT: Failed casting to float
    :return: volumeSphere(value)
    :rtype: float2
    """
    if(re.match(r'^([0-9]*\.?[0-9]*)(e-?[0-9]+)?$', line) and (line != '.')):
        try:
            value = float(line)
            return volumeSphere(value)
        except:
            raise Exception(200, "BAD INPUT: Failed casting to float")
    else:
        raise Exception(100, "BAD INPUT: Not a positive number")


if __name__ == "__main__":
    if(len(sys.argv) > 1):
        try:
            f = open(sys.argv[1], "r")
        except:
            print("Error while opening file")
        for line in f.readlines():
            try:
                result = main(line.strip())
            except Exception as exception:
                error_code = exception.args[0]
                error_msg = exception.args[1]
                print(error_msg + ', error code : ' + str(error_code))
            else:
                print(round(result, 8))
    else:
        print("Error: you must enter file name")
