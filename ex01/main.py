import sys
import re

class NumberValuesException(Exception):
    """Too much or less numbers"""

def main(line):

    values = line.split(';')
    try:
        if((len(values) == 2) and (values[0] != '') and (values[1] != '')):
            if(re.match('^[0-9]*\.?[0-9]*$', values[0]) and re.match('^[0-9]*\.?[0-9]*$', values[1])):
                time = float(values[0])
                distance = float(values[1])
                if(time > 0):
                    speed = distance/time
                    return speed
                else:
                    print("1.2 BAD INPUT: Time must be greater than 0!")
            else:
                print("1.1 BAD INPUT: Values are not digits or are less than 0!")
        else:
            raise NumberValuesException
    except NumberValuesException:
        print("1.0 BAD INPUT: You need to enter 2 values")

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        try:
            f = open(sys.argv[1], "r")
        except:
            print("Error while opening file")
        for line in f.readlines():
            speed = main(line.strip())
            if(speed):
                print("Speed = " + str(round(speed, 1)) + " m/s")
    else:
        print("Error: you must enter file name")