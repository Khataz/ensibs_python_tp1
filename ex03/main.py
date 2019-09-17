import sys
import re

def main(line):

    values = line.split(';')
    if((len(values) == 2) and (values[0] != '') and (values[1] != '')):
        if(re.match(r'^\w*$', values[0]) and re.match(r'^\w*$', values[1])):
            word1 = values[0]
            word2 = values[1]

            """True = same words"""
            if(word1 < word2):
                return word1, False
            elif(word2 < word1):
                return word2, False
            elif(word1 == word2):
                return word1, True
            else:
                raise Exception(300, "ERROR: The program failed to compare the two words")
        else:
            raise Exception(200, "BAD INPUT: Values are not words! (Sentences are not allowed)")
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
                if(result[1]):
                    print("Words '" + result[0] + "' are equals")
                else:
                    print("Smallest word = '" + result[0] + "'")
    else:
        print("Error: you must enter file name")