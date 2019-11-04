import main
import unittest


class TestMainMethods(unittest.TestCase):
    def test_working(self):
        expectedArray = ['ad', 'ae', 'bd', 'be', 'cd', 'ce']
        self.assertEqual(main.main("abc", "de"), expectedArray)


if __name__ == '__main__':
    unittest.main()
