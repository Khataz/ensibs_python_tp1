class Vecteur2D:

    x = 0
    y = 0

    def __init__(self, valX = 0, valY = 0):
        """Constructeur de notre classe. Si aucun paramètre n'est précisé, le vecteur sera de (0;0)"""
        self.x = valX
        self.y = valY

    def affiche(self):
        print(self.x,self.y)

    def __add__(self, v2):
        return(Vecteur2D(self.x+v2.x, self.y+v2.y))


if __name__ == "__main__":
    v1 = Vecteur2D()
    v1.affiche()

    v2 = Vecteur2D(3, 4)
    v2.affiche()

    v3 = Vecteur2D(4, 6)

    v4 = v2+v3
    v4.affiche()