import main
import unittest


class TestMainMethods(unittest.TestCase):

    def test_maFonction(self):
        self.assertEqual(main.maFonction(1), -2)

    def test_working(self):
        expected_ret1 = [-2.0, 13.0]
        self.assertEqual(main.main("maFonction;1;2;1"), expected_ret1)
        expected_ret2 = [-443.0, -137.0, -23.0, -5.0, 13.0, 127.0, 433.0]
        self.assertEqual(main.main("maFonction;-6;6;2"), expected_ret2)
    
    def test_not_a_float(self):
        with self.assertRaises(Exception) as e:
            main.main('maFonction;a;10;1')
        self.assertTrue(e.exception.args[0] == 100)

        with self.assertRaises(Exception) as e:
            main.main('maFonction;10;a;1')
        self.assertTrue(e.exception.args[0] == 110)

        with self.assertRaises(Exception) as e:
            main.main('maFonction;10;10;a')
        self.assertTrue(e.exception.args[0] == 120)

    def test_boundary_error(self):
        with self.assertRaises(Exception) as e:
            main.main('maFonction;11;10;1')
        self.assertTrue(e.exception.args[0] == 300)

        with self.assertRaises(Exception) as e:
            main.main('maFonction;-10;-11;1')
        self.assertTrue(e.exception.args[0] == 300)

    def test_function_error(self):
        with self.assertRaises(Exception) as e:
            main.main('abc;11;10;1')
        self.assertTrue(e.exception.args[0] == 30)
    
if __name__ == '__main__':
    unittest.main()
