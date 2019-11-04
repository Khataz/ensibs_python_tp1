import sys
import re
from numpy import arange


def maFonction(x):
    """
    Compute f(x)=2x³+x-5

    @param x: x value
    @type x: float
    @raise Exception: if BAD INPUT
    @return res
    @rtype float
    """
    res = 2 * (x**3) + x - 5
    return res


def tabuler(fonction, borneInf, borneSup, nbPas):
    """
    Compute square root of a number.

    @param fonction: function(x)
    @type fonction: function
    @param borneInf: lower boundary
    @type borneInf: float
    @param borneSup: higher boundary
    @type borneSup: float
    @param nbPas: step
    @type nbPas: int
    @return value
    @rtype array[float]
    """
    if borneInf < borneSup:
        # TODO check boundary in new subject"""
        ret = []
        for i in arange(borneInf, borneSup + 1, nbPas):
            ret.append(fonction(i))
    else:
        raise Exception(
            300, "BAD INPUT: borneInf must be lower than borneSup")
    return ret


def main(line):
    """
    Check line then call tabuler.

    @param line: line readed from file containing 3 floats (borneInf;borneSup;nbPas)
    @type line: string
    @raise Exception: if BAD INPUT
    @return /
    @rtype array[float]

    @todo check why it continue after raised error
    """
    values = line.split(';')
    regex = r"-?([0-9]*\.?[0-9]*)(e-?[0-9]+)?$"
    if len(values) == 3:
        if re.match(str(regex), str(values[0])) and values[0] != '.':
            try:
                borneInf = float(values[0])
            except:
                raise Exception(
                    200, "BAD INPUT: Failed casting borneInf to float")
            else:
                if re.match(str(regex), str(values[1])) and values[1] != '.':
                    try:
                        borneSup = float(values[1])
                    except:
                        raise Exception(
                            210, "BAD INPUT: Failed casting borneSup to float")
                    else:
                        if re.match(str(regex), str(values[2])) and values[2] != '.':
                            try:
                                nbPas = int(values[2])
                                if nbPas <= 0:
                                    raise Exception(
                                        230, "BAD INPUT: nbPas must be positive")
                            except:
                                raise Exception(
                                    220, "BAD INPUT: Failed casting nbPas to float")
                            '''else:
                                ret = tabuler(maFonction, borneInf, borneSup, nbPas)'''
                        else:
                            raise Exception(
                                120, "BAD INPUT: nbPas is not a float")
                else:
                    raise Exception(110, "BAD INPUT: borneSup is not a float")
        else:
            raise Exception(100, "BAD INPUT: borneInf is not a float")
    else:
        raise Exception(
            10, "BAD INPUT: you need to pass 3 args : borneInf, borneSup, nbPas")

    ret = tabuler(maFonction, borneInf, borneSup, nbPas)
    return ret


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
        print("Error: you must enter a file name")
