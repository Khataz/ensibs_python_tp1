#!/usr/bin/env python3 -W ignore::DeprecationWarning
import main
import unittest

class TestMainMethods(unittest.TestCase):
    def test_working(self):
        self.assertEqual(main.main("6;9"), 1.5)
        #To refactor (separe in some functions)

    def test_too_much_values(self):
        # with self.assertRaises(main.NumberValuesException) as too_much_values:
        #     main.main('10;4;01')
        # self.assertTrue("1.0 BAD INPUT: You need to enter 2 values" in too_much_values.exception)     
        #self.assertRaises(main.NumberValuesException, main.main('10;4;01'))

        # can we work on E to check error code ?
        with self.assertRaises(Exception) as E:
            res = main.main('10;4;01')


    # def test_not_enought_values(self):
    #     self.assertEqual(str(main.main("10")).find("1.0 BAD INPUT"), -1)
    #     self.assertEqual(str(main.main("10;")).find("1.0 BAD INPUT"), -1)
    

    # def test_value_0_is_not_a_digit(self):
    #     self.assertEqual(str(main.main("1a4;10")).find("1.1 BAD INPUT"), -1)
    #     self.assertEqual(str(main.main("aaaa;10")).find("1.1 BAD INPUT"), -1)
    #     self.assertEqual(str(main.main("$;10")).find("1.1 BAD INPUT"), -1)
    #     self.assertEqual(str(main.main("4;10")).find("1.1 BAD INPUT"), -1)

    # def test_value_1_is_not_a_digit(self):
    #     #TODO
    # def test_time_equals_0(self);
    #     #TODO
    

if __name__ == '__main__':
    unittest.main()