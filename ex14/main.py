class MaClasse:
    """
        Classe MaClasse.
    """
    x = 23
    y = x + 5

    def affiche(self):
        """
        Print (self.y, z)

        :param none:
        :return: none
        """
        z = 42
        print("(" + str(self.y) + ", " + str(z) + ")")


if __name__ == "__main__":
    maClasse1 = MaClasse()
    maClasse1.affiche()
