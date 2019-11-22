import main
import unittest


class TestMaClasse(unittest.TestCase):
    def test_working(self):
        instance = main.MaClasse()
        self.assertEquals(instance.__class__.__name__, "MaClasse")


if __name__ == '__main__':
    unittest.main()
