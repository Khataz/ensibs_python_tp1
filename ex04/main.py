import sys
import re

OK = "OK"
STOP = "STOP"
INCREASE_VOLUME = "INCREASE_VOLUME"
DECREASE_VOLUME = "DECREASE_VOLUME"

def main(line):
    pThreshold = 2.3
    vThreshold = 7.41

    values = line.split(';')
    if((len(values) == 2) and (values[0] != '') and (values[1] != '') and (values[0] != '.' and values[1] != '.')):
        if(re.match(r'^[0-9]*\.?[0-9]*$', values[0]) and re.match(r'^[0-9]*\.?[0-9]*$', values[1])):
            pressure = float(values[0])
            volume = float(values[1])
            if((pressure > pThreshold) and (volume > vThreshold)):
                return STOP
            elif((pressure > pThreshold) and (volume >= 0)):
                return INCREASE_VOLUME
            elif((volume > vThreshold) and (pressure >= 0)):
                return DECREASE_VOLUME
            else:
                return OK
        else:
            raise Exception(200, "BAD INPUT: Values are not digits or are less than 0!")
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
                result = main(line.strip())
            except Exception as exception :
                error_code = exception.args[0]
                error_msg = exception.args[1]
                print(error_msg + ', error code : ' + str(error_code))
            else :
                if(result == STOP):
                    print("STOPPING SYSTEM...")
                elif(result == INCREASE_VOLUME):
                    print("You need to INCREASE the volume of the enclosure!")
                elif(result == DECREASE_VOLUME):
                    print("You need to DECREASE the volume of the enclosure!")
                else:
                    print("Everything is fine!")
    else:
        print("Error: you must enter file name")