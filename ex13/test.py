import main
import unittest


class TestMainMethods(unittest.TestCase):

    def test_CompterMots_one_word(self):
        expected = {'hello':1}
        test_value = "hello"
        self.assertEqual(main.CompterMots(test_value), expected)

    def test_CompterMots_two_words(self):
        expected = {'hello':1, 'world': 1}
        test_value = "hello world"
        self.assertEqual(main.CompterMots(test_value), expected)

    def test_CompterMots_tree_word(self):
        expected = {'hello':2, 'world': 2}
        test_value = "hello  world  hello   world"
        self.assertEqual(main.CompterMots(test_value), expected)

if __name__ == '__main__':
    unittest.main()
