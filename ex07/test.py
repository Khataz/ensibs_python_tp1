import main
import unittest


class TestMainMethods(unittest.TestCase):

    def test_maFonction(self):
        self.assertEqual(main.maFonction(1), -2)

    def test_working(self):
        expected_ret1 = [-2.0, 13.0]
        self.assertEqual(main.main("1;2;1"), expected_ret1)
        expected_ret2 = [-443.0, -137.0, -23.0, -5.0, 13.0, 127.0, 433.0]
        self.assertEqual(main.main("-6;6;2"), expected_ret2)
    
    def test_not_a_float(self):
        with self.assertRaises(Exception) as e:
            main.main('a;10;1')
        self.assertTrue(e.exception.args[0] == 100)

        with self.assertRaises(Exception) as e:
            main.main('10;a;1')
        self.assertTrue(e.exception.args[0] == 110)

        with self.assertRaises(Exception) as e:
            main.main('10;10;a')
        self.assertTrue(e.exception.args[0] == 120)

    def test_boundary_error(self):
        with self.assertRaises(Exception) as e:
            main.main('11;10;1')
        self.assertTrue(e.exception.args[0] == 300)

        with self.assertRaises(Exception) as e:
            main.main('-10;-11;1')
        self.assertTrue(e.exception.args[0] == 300)
    
if __name__ == '__main__':
    unittest.main()
