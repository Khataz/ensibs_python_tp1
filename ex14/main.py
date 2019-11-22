class MaClasse:
    x = 23
    y = x+5

    def affiche(self):
        z = 42
        print("y = " + str(MaClasse.y))
        print("z = " + str(z))

if __name__ == "__main__":
    maClasse1 = MaClasse()
    maClasse1.affiche()