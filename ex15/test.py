import main
import unittest


class TestMaClasse(unittest.TestCase):
    def test_working(self):
        v1 = main.Vecteur2D()
        v2 = main.Vecteur2D(3, 4)

        self.assertEquals(v1.x, 0)
        self.assertEquals(v1.y, 0)

        self.assertEquals(v2.x, 3)
        self.assertEquals(v2.y, 4)


if __name__ == '__main__':
    unittest.main()
