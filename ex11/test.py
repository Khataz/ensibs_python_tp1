import main
import unittest


class TestMainMethods(unittest.TestCase):
    def test_working(self):
        expectedArray = [0, 1, 2, 6, 7, 8]
        self.assertEqual(main.main(), expectedArray)


if __name__ == '__main__':
    unittest.main()
