import sys
import re


def CompterMots(sentence):
    """
    Return the number of occurence of each word in sentence.

    :param sentence: line in input
    :type sentence: string
    :raises Exception: 100 - BAD INPUT: You need to enter 2 values
    :raises Exception: 200 - BAD INPUT: Values are not digits or are less than 0!
    :return: {'word1': nbOfWord1, 'word2': nbOfWord2, ...}
    :rtype: {'STR': INT, 'STR': INT, ...}
    """
    # TODO:I allowed '-' to count as char, is that right, see regex
    if re.match(r'^[a-zA-Z]+((\ *|-)?[a-zA-Z]+)*.?$', sentence):
        words = sentence.split()
        words.sort()
        ret = {e: sentence.count(e) for e in words}

        return ret
    else:
        raise Exception(100, "BAD INPUT: Not a sentence composed by words.")


def main(line):
    try:
        sentence = str(line)

        return CompterMots(sentence)
    except:
        raise Exception(200, "BAD INPUT: Failed casting to str")


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
                print(str(result))
    else:
        print("Error: you must enter file name")
