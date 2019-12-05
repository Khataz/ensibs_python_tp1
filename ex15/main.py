import sys
import re


class Vecteur2D:
    """
        Class Vecteur2D : two dimensions vector class.
    """

    x = 0
    y = 0

    def __init__(self, valX=0, valY=0):
        """
            Class constructor.
            If no parameters, (0;0) is returned.
        """
        self.x = valX
        self.y = valY

    def affiche(self):
        """
        Print (self.y, z)

        :param none:
        :return: none
        """
        print("(x=" + str(self.x) + ", y=" + str(self.y) + ")")


def main(line):
    """
    Return the a Vecteur2D.

    :param line: line in input, format : FLOAT<x>;FLOAT<y>
    :type line: string
    :raises Exception: 100 - BAD INPUT: You need to enter 2 values
    :raises Exception: 200 - BAD INPUT: Values are not digits!
    :return: Vecteur2D(x,y)
    :rtype: Vecteur2D
    """

    values = line.split(';')
    if((len(values) == 2) and (values[0] != '') and (values[1] != '') and (values[0] != '.' and values[1] != '.')):
        if(re.match(r'^-?[0-9]*\.?[0-9]*$', values[0]) and re.match(r'^-?[0-9]*\.?[0-9]*$', values[1])):
            return Vecteur2D(values[0], values[1])
        else:
            raise Exception(
                200, "BAD INPUT: Values are not digits!")
    else:
        raise Exception(100, "BAD INPUT: You need to enter 2 values")


if __name__ == "__main__":
    v1 = Vecteur2D()

    print("par défaut :", end=" ")
    v1.affiche()

    if(len(sys.argv) > 1):
        try:
            f = open(sys.argv[1], "r")
        except:
            print("Error while opening file")
        for line in f.readlines():
            try:
                v = main(line.strip())
            except Exception as exception:
                error_code = exception.args[0]
                error_msg = exception.args[1]
                print(error_msg + ', error code : ' + str(error_code))
            else:
                print("instance :", end=" ")
                v.affiche()
    else:
        print("Error: you must enter file name")
