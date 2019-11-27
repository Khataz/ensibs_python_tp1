import main
import unittest


class TestMainMethods(unittest.TestCase):
    def test_good_tchacatchac(self):
        self.assertEqual(main.tchacatchac(100), "10:42")
        self.assertEqual(main.tchacatchac(110), "10:32")
        self.assertEqual(main.tchacatchac(120), "10:25")
        self.assertEqual(main.tchacatchac(130), "10:18")
        self.assertEqual(main.tchacatchac(140), "10:12")
        self.assertEqual(main.tchacatchac(150), "10:8")
        self.assertEqual(main.tchacatchac(160), "10:3")
        self.assertEqual(main.tchacatchac(170), "10:0")
        self.assertEqual(main.tchacatchac(180), "9:56")
        self.assertEqual(main.tchacatchac(190), "9:53")
        self.assertEqual(main.tchacatchac(200), "9:51")
        self.assertEqual(main.tchacatchac(210), "9:48")
        self.assertEqual(main.tchacatchac(220), "9:46")
        self.assertEqual(main.tchacatchac(230), "9:44")
        self.assertEqual(main.tchacatchac(240), "9:42")
        self.assertEqual(main.tchacatchac(250), "9:40")
        self.assertEqual(main.tchacatchac(260), "9:39")
        self.assertEqual(main.tchacatchac(270), "9:37")
        self.assertEqual(main.tchacatchac(280), "9:36")
        self.assertEqual(main.tchacatchac(290), "9:35")
        self.assertEqual(main.tchacatchac(300), "9:34")

    def test_bad_tchacatchac(self):
        with self.assertRaises(Exception) as e:
            main.tchacatchac(-3)
        self.assertTrue(e.exception.args[0] == 100)

if __name__ == '__main__':
    unittest.main()
