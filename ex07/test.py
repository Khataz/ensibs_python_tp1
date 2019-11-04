import main
import unittest


class TestMainMethods(unittest.TestCase):
    def test_working(self):
        # TODO : compute values
        self.assertEqual(main.main("9."), 3)

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
            main.main('-11;-10;1')
        self.assertTrue(e.exception.args[0] == 300)

if __name__ == '__main__':
    unittest.main()
