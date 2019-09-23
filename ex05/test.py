import main
import unittest


class TestMainMethods(unittest.TestCase):
    def test_working(self):
        expectedArray = [0, 3, 6, 9, 12]
        self.assertEqual(main.main(), expectedArray)


if __name__ == '__main__':
    unittest.main()
