import main
import unittest


class TestMainMethods(unittest.TestCase):

    # Original list: [17, 38, 10, 25, 72]

    def test_function1(self):
        self.assertEqual(main.function1(), ({'a', 'b', 'c', 'd'}, {'s', 'b', 'd'}))
    
    def test_function2(self):
        self.assertEqual(main.function2(), True)

    def test_function3(self):
        self.assertEqual(main.function3(), False)

    def test_function4(self):
        self.assertEqual(main.function4(), {'a', 'c'})

    def test_function5(self):
        self.assertEqual(main.function5(), {'s'})

    def test_function6(self):
        self.assertEqual(main.function6(), {'a', 'b', 'c', 'd', 's'})

    def test_function7(self):
        self.assertEqual(main.function7(), {'b', 'd'})

if __name__ == '__main__':
    unittest.main()
