import main
import unittest


class TestMainMethods(unittest.TestCase):
    def test_working(self):
        self.assertEqual(main.main("9."), 3)
        self.assertEqual(main.main("2.0"), 1.4142135623730951)
        self.assertEqual(main.main("3.14"), 1.772004514666935)
        self.assertEqual(main.main("2.0e-1"), 0.4472135954999579)

    def test_not_a_float(self):
        with self.assertRaises(Exception) as e:
            main.main('10')
        self.assertTrue(e.exception.args[0] == 100)

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

    def test_negative_floats(self):
        with self.assertRaises(Exception) as e:
            main.main('-1.')
        self.assertTrue(e.exception.args[0] == 100)

        with self.assertRaises(Exception) as e:
            main.main('-2.0e-1')
        self.assertTrue(e.exception.args[0] == 100)


if __name__ == '__main__':
    unittest.main()
