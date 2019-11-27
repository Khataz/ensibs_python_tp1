import main
import unittest


class TestMaClasse(unittest.TestCase):
    def test_working(self):
        v1 = main.Vecteur2D()
        v2 = main.Vecteur2D(3, 4)
        v3 = main.Vecteur2D(4, 6)
        v4 = v2+v3

        self.assertEquals(v1.x, 0)
        self.assertEquals(v1.y, 0)

        self.assertEquals(v2.x, 3)
        self.assertEquals(v2.y, 4)

        self.assertEquals(v4.x, 7)
        self.assertEquals(v4.y, 10)


if __name__ == '__main__':
    unittest.main()
