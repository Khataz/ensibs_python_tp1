import re

distance = 170

def splitTime(hour):
    print(hour)
    splittedTime = str(hour).split('.')
    hour = int(splittedTime[0])

    minute = 0

    if(len(splittedTime) == 2):
        minute = "0." + splittedTime[1][0:2]
        print("LIMITED = " + minute)
        print(minute)
        minute = float(minute)*60
        print("mins: " + minute)
        minute = int(minute.split('.')[0])
    return (hour,minute)

    //TODO

def tchacatchac(speed):
    if(re.match(r'^([0-9]*\.?[0-9]*)(e-?[0-9]+)?$', str(speed)) and (str(speed) != '.')):
        try:
            hour,minute = splitTime(distance/speed)
            hour += 9

            return (str(hour) + "h et " + str(minute) + "min" )
        except:
            raise Exception(200, "BAD INPUT: Failed casting to float")
    else:
        raise Exception(100, "BAD INPUT: Not a positive number")

if __name__ == "__main__":
    # result = []
    # for speed in range(100, 300, 10):
    #     result.append(tchacatchac(speed))

    # print(result)

    print(tchacatchac(110))