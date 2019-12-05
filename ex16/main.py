import sys
import re


class Vecteur2D:

    x = 0
    y = 0

    def __init__(self, valX=0, valY=0):
        """Constructeur de notre classe. Si aucun paramètre n'est précisé, le vecteur sera de (0;0)"""
        self.x = valX
        self.y = valY

    def affiche(self):
        """
        Print (self.y, z)

        :param none:
        :return: none
        """
        print("(x=" + str(self.x) + ", y=" + str(self.y) + ")")

    def __add__(self, v2):
        """
        Add this vector plus v2

        :param v2:
        :type v2: Vecteur2D
        :return: new Vecteur2D( (v1.x)+(v2.x), (v1.y)+(v2.y)
        :rtype: Vecteur2D
        """
        return(Vecteur2D(float(self.x) + float(v2.x), float(self.y) + float(v2.y)))


def main(line):
    values = line.split(';')
    if((len(values) == 4) and (values[0] != '') and (values[1] != '') and (values[2] != '') and (values[3] != '') and (values[0] != '.') and (values[1] != '.') and (values[2] != '.') and (values[3] != '.')):
        if(re.match(r'^-?[0-9]*\.?[0-9]*$', values[0]) and re.match(r'^-?[0-9]*\.?[0-9]*$', values[1]) and re.match(r'^-?[0-9]*\.?[0-9]*$', values[2]) and re.match(r'^-?[0-9]*\.?[0-9]*$', values[3])):
            return (Vecteur2D(values[0], values[1]), Vecteur2D(values[2], values[3]))
        else:
            raise Exception(200, "BAD INPUT: Values are not digits!")
    else:
        raise Exception(100, "BAD INPUT: You need to enter 4 values")


if __name__ == "__main__":
    if(len(sys.argv) > 1):
        try:
            f = open(sys.argv[1], "r")
        except:
            print("Error while opening file")
        for line in f.readlines():
            try:
                (v1, v2) = main(line.strip())
            except Exception as exception:
                error_code = exception.args[0]
                error_msg = exception.args[1]
                print(error_msg + ', error code : ' + str(error_code))
            else:
                print("v1 :", end=" ")
                v1.affiche()

                print("v2 :", end=" ")
                v2.affiche()

                sumResult = v1 + v2
                print("somme :", end=" ")
                sumResult.affiche()
    else:
        print("Error: you must enter file name")
