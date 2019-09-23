import sys
import re
import numpy as np

def cube(value):
    return value**3

def volumeSphere(r):
    return 4 / 3 * np.pi * cube(r)

def main(line):
    if(re.match(r'^([0-9]*\.?[0-9]*)(e-?[0-9]+)?$', line) and (line != '.')):
        # TODO: Test if we allow all floats
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
                print("Sphere volume = " + str(result))
    else:
        print("Error: you must enter file name")