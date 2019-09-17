import main
import unittest

class TestMainMethods(unittest.TestCase):
    def test_working(self):
        self.assertEqual(main.main("6;9"), 1.5)
        #To refactor (separe in some functions)

    def test_too_much_values(self):
        with self.assertRaises(Exception) as e:
            main.main('10;4;10')
        self.assertTrue(e.exception[0] == 10)
        with self.assertRaises(Exception) as e:
            main.main('10;4678;')
        self.assertTrue(e.exception[0] == 10)

    def test_not_enought_values(self):
        with self.assertRaises(Exception) as e:
            main.main('65;')
        self.assertTrue(e.exception[0] == 10)
        with self.assertRaises(Exception) as e:
            main.main('100')
        self.assertTrue(e.exception[0] == 10)
        with self.assertRaises(Exception) as e:
            main.main('')
        self.assertTrue(e.exception[0] == 10)
    
    def test_value_0_is_not_a_digit(self):
        with self.assertRaises(Exception) as e:
            main.main('1a4;10')
        self.assertTrue(e.exception[0] == 11)
        with self.assertRaises(Exception) as e:
            main.main('aaaa;10')
        self.assertTrue(e.exception[0] == 11)
        with self.assertRaises(Exception) as e:
            main.main('$;10')
        self.assertTrue(e.exception[0] == 11)

    def test_value_1_is_not_a_digit(self):
        with self.assertRaises(Exception) as e:
            main.main('308;1groh0')
        self.assertTrue(e.exception[0] == 11)
        with self.assertRaises(Exception) as e:
            main.main('3480;thro')
        self.assertTrue(e.exception[0] == 11)
        with self.assertRaises(Exception) as e:
            main.main('350;$')
        self.assertTrue(e.exception[0] == 11)

    # def test_time_equals_0(self);
    #     #TODO
    
    #TODO: CHECK IF ENTERED ";" !

if __name__ == '__main__':
    unittest.main()