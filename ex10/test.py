import main
import unittest


class TestMainMethods(unittest.TestCase):
    def test_working(self):
        expectedArray = [0, 1, 2, 6, 7, 8]
        self.assertEqual(main.main([0, 1, 2, 3, 4, 5]), expectedArray)


if __name__ == '__main__':
    unittest.main()
