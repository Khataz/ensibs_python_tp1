import main
import unittest

class TestMainMethods(unittest.TestCase):
    def test_working(self):
        self.assertEqual(main.main("2;4"), main.OK)
        self.assertEqual(main.main("6;9"), main.STOP)
        self.assertEqual(main.main("2;40"), main.DECREASE_VOLUME)
        self.assertEqual(main.main("2038;4"), main.INCREASE_VOLUME)

    def test_too_much_values(self):
        with self.assertRaises(Exception) as e:
            main.main('10;4;10')
        self.assertTrue(e.exception.args[0] == 100)

        with self.assertRaises(Exception) as e:
            main.main('10;4678;')
        self.assertTrue(e.exception.args[0] == 100)

    def test_not_enought_values(self):
        with self.assertRaises(Exception) as e:
            main.main('65;')
        self.assertTrue(e.exception.args[0] == 100)
        with self.assertRaises(Exception) as e:
            main.main('100')
        self.assertTrue(e.exception.args[0] == 100)
        with self.assertRaises(Exception) as e:
            main.main('')
        self.assertTrue(e.exception.args[0] == 100)
    
    def test_value_0_is_bad(self):
        with self.assertRaises(Exception) as e:
            main.main('1a4;10')
        self.assertTrue(e.exception.args[0] == 200)
        with self.assertRaises(Exception) as e:
            main.main('aaaa;10')
        self.assertTrue(e.exception.args[0] == 200)
        with self.assertRaises(Exception) as e:
            main.main('$;10')
        self.assertTrue(e.exception.args[0] == 200)
        with self.assertRaises(Exception) as e:
            main.main('-248;2508')
        self.assertTrue(e.exception.args[0] == 200)

    def test_value_1_is_bad(self):
        with self.assertRaises(Exception) as e:
            main.main('308;1groh0')
        self.assertTrue(e.exception.args[0] == 200)
        with self.assertRaises(Exception) as e:
            main.main('3480;thro')
        self.assertTrue(e.exception.args[0] == 200)
        with self.assertRaises(Exception) as e:
            main.main('350;$')
        self.assertTrue(e.exception.args[0] == 200)
        with self.assertRaises(Exception) as e:
            main.main('0248;-5')
        self.assertTrue(e.exception.args[0] == 200)

if __name__ == '__main__':
    unittest.main()