import sys
import re


def main(line):
    """
    Return the speed.

    After sanitizing the input (line), this function compute the speed.

    :param line: line in input, format : FLOAT<temps>;FLOAT<distance>
    :type line: string
    :raises Exception: 100 - BAD INPUT: You need to enter 2 values
    :raises Exception: 200 - BAD INPUT: Values are not digits or are less than 0!
    :raises Exception: 300 - BAD INPUT: Time must be greater than 0!
    :return: speed
    :rtype: float2
    """
    values = line.split(';')
    if((len(values) == 2) and (values[0] != '') and (values[1] != '') and (values[0] != '.' and values[1] != '.')):
        if(re.match(r'^[0-9]*\.?[0-9]*$', values[0]) and re.match(r'^[0-9]*\.?[0-9]*$', values[1])):
            time = float(values[0])
            distance = float(values[1])
            if(time > 0):
                speed = distance / time
                return speed
            else:
                raise Exception(300, "BAD INPUT: Time must be greater than 0!")
        else:
            raise Exception(
                200, "BAD INPUT: Values are not digits or are less than 0!")
    else:
        raise Exception(100, "BAD INPUT: You need to enter 2 values")


if __name__ == "__main__":
    if(len(sys.argv) > 1):
        try:
            f = open(sys.argv[1], "r")
        except:
            print("Error while opening file")
        for line in f.readlines():
            try:
                speed = main(line.strip())
            except Exception as exception:
                error_code = exception.args[0]
                error_msg = exception.args[1]
                print(error_msg + ', error code : ' + str(error_code))
            else:
                print(round(speed, 8))
    else:
        print("Error: you must enter file name")
