import main
import unittest


class TestMainMethods(unittest.TestCase):
    def test_good_tchacatchac(self):
        self.assertEqual(main.tchacatchac(100), "10h et 42min")
        self.assertEqual(main.tchacatchac(110), "10h et 32min")
        self.assertEqual(main.tchacatchac(120), "10h et 25min")
        self.assertEqual(main.tchacatchac(130), "10h et 18min")
        self.assertEqual(main.tchacatchac(140), "10h et 12min")
        self.assertEqual(main.tchacatchac(150), "10h et 8min")
        self.assertEqual(main.tchacatchac(160), "10h et 3min")
        self.assertEqual(main.tchacatchac(170), "10h et 0min")
        self.assertEqual(main.tchacatchac(180), "9h et 56min")
        self.assertEqual(main.tchacatchac(190), "9h et 53min")
        self.assertEqual(main.tchacatchac(200), "9h et 51min")
        self.assertEqual(main.tchacatchac(210), "9h et 48min")
        self.assertEqual(main.tchacatchac(220), "9h et 46min")
        self.assertEqual(main.tchacatchac(230), "9h et 44min")
        self.assertEqual(main.tchacatchac(240), "9h et 42min")
        self.assertEqual(main.tchacatchac(250), "9h et 40min")
        self.assertEqual(main.tchacatchac(260), "9h et 39min")
        self.assertEqual(main.tchacatchac(270), "9h et 37min")
        self.assertEqual(main.tchacatchac(280), "9h et 36min")
        self.assertEqual(main.tchacatchac(290), "9h et 35min")
        self.assertEqual(main.tchacatchac(300), "9h et 34min")

    def test_bad_tchacatchac(self):
        with self.assertRaises(Exception) as e:
            main.tchacatchac(-3)
        self.assertTrue(e.exception.args[0] == 100)

if __name__ == '__main__':
    unittest.main()
