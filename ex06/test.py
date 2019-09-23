import main
import unittest


class TestMainMethods(unittest.TestCase):
    def test_working(self):
        self.assertEqual(round(main.main("9"), 2), 3053.63)
        self.assertEqual(round(main.main("2.0"), 2), 33.51)
        self.assertEqual(round(main.main("3.14"), 2), 129.68)
        self.assertEqual(round(main.main("2.0e-1"), 2), 0.03)

    def test_not_a_number(self):
        with self.assertRaises(Exception) as e:
            main.main('10,0')
        self.assertTrue(e.exception.args[0] == 100)

        with self.assertRaises(Exception) as e:
            main.main(',0')
        self.assertTrue(e.exception.args[0] == 100)

        with self.assertRaises(Exception) as e:
            main.main('2;1')
        self.assertTrue(e.exception.args[0] == 100)

        with self.assertRaises(Exception) as e:
            main.main('a')
        self.assertTrue(e.exception.args[0] == 100)

    def test_negative_numbers(self):
        with self.assertRaises(Exception) as e:
            main.main('-1.')
        self.assertTrue(e.exception.args[0] == 100)

        with self.assertRaises(Exception) as e:
            main.main('-2.0e-1')
        self.assertTrue(e.exception.args[0] == 100)
        
        with self.assertRaises(Exception) as e:
            main.main('-4508')
        self.assertTrue(e.exception.args[0] == 100)


if __name__ == '__main__':
    unittest.main()
