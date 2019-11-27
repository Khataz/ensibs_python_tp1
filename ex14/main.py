class MaClasse:
    x = 23
    y = x+5

    def affiche(self):
        z = 42
        print("(" + str(self.y) + ", " + str(z) + ")")

if __name__ == "__main__":
    maClasse1 = MaClasse()
    maClasse1.affiche()