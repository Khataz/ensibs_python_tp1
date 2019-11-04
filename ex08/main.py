import re

distance = 170

def splitTime(hour):
    splittedTime = str(hour).split('.')
    hour = int(splittedTime[0])

    minute = 0

    if(len(splittedTime) == 2):
        minute = "0." + splittedTime[1]
        minute = round(float(minute)*60, 10)
        minute = str(minute)
        minute = int(minute.split('.')[0])
    return (hour,minute)

def tchacatchac(speed):
    if(re.match(r'^([0-9]*\.?[0-9]*)(e-?[0-9]+)?$', str(speed)) and (str(speed) != '.')):
        try:
            hour,minute = splitTime(float(distance)/float(speed))
            hour += 9

            return (str(hour) + "h et " + str(minute) + "min" )
        except:
            raise Exception(200, "BAD INPUT: Failed casting to float")
    else:
        raise Exception(100, "BAD INPUT: Not a positive number")

if __name__ == "__main__":
    result = []
    for speed in range(100, 310, 10):
        result.append(tchacatchac(speed))

    print(result)