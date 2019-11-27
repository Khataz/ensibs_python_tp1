class Vecteur2D:

    x = 0
    y = 0

    def __init__(self, valX = 0, valY = 0):
        """Constructeur de notre classe. Si aucun paramètre n'est précisé, le vecteur sera de (0;0)"""
        self.x = valX
        self.y = valY

    def affiche(self):
        print(self.x,self.y)

if __name__ == "__main__":
    v1 = Vecteur2D()
    v2 = Vecteur2D(3, 4)

    v1.affiche()
    v2.affiche()