import sys
import re

class Vecteur2D:

    x = 0
    y = 0

    def __init__(self, valX = 0, valY = 0):
        """Constructeur de notre classe. Si aucun paramètre n'est précisé, le vecteur sera de (0;0)"""
        self.x = valX
        self.y = valY

    def affiche(self):
        print("(x=" + str(self.x) + ", y=" + str(self.y) + ")")

def main(line):

    values = line.split(';')
    if((len(values) == 2) and (values[0] != '') and (values[1] != '') and (values[0] != '.' and values[1] != '.')):
        if(re.match(r'^-?[0-9]*\.?[0-9]*$', values[0]) and re.match(r'^-?[0-9]*\.?[0-9]*$', values[1])):
            return Vecteur2D(values[0], values[1])
        else:
            raise Exception(
                200, "BAD INPUT: Values are not digits or are less than 0!")
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
                print("instance :", end = " ")
                v.affiche()
    else:
        print("Error: you must enter file name")