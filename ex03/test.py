import main
import unittest


class TestMainMethods(unittest.TestCase):
    def test_working(self):
        self.assertEqual(main.main("salut;amour"), ("amour", False))

    def test_not_enought_values(self):
        with self.assertRaises(Exception) as e:
            main.main(';')
        self.assertTrue(e.exception.args[0] == 100)

        with self.assertRaises(Exception) as e:
            main.main('hello;')
        self.assertTrue(e.exception.args[0] == 100)

        with self.assertRaises(Exception) as e:
            main.main(';bonsoir')
        self.assertTrue(e.exception.args[0] == 100)

    def test_values_are_not_words(self):
        with self.assertRaises(Exception) as e:
            main.main('salut toto; yo')
        self.assertTrue(e.exception.args[0] == 200)
        
        with self.assertRaises(Exception) as e:
            main.main('salut ;yo')
        self.assertTrue(e.exception.args[0] == 200)

        with self.assertRaises(Exception) as e:
            main.main('mère;coucou ')
        self.assertTrue(e.exception.args[0] == 200)

if __name__ == '__main__':
    unittest.main()
