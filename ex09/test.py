import main
import unittest


class TestMainMethods(unittest.TestCase):

    # Original list: [17, 38, 10, 25, 72]

    def test_function1(self):
        self.assertEqual(main.function1(main.originalList.copy()), [10, 17, 25, 38, 72])
    
    def test_function2(self):
        self.assertEqual(main.function2(main.originalList.copy()), [17, 38, 10, 25, 72, 12])

    def test_function3(self):
        self.assertEqual(main.function3(main.originalList.copy()), [72, 25, 10, 38, 17])

    def test_function4(self):
        self.assertEqual(main.function4(main.originalList.copy()), 0)

    def test_function5(self):
        self.assertEqual(main.function5(main.originalList.copy()), [17, 10, 25, 72])

    def test_function6(self):
        self.assertEqual(main.function6(main.originalList.copy()), [38, 10])

    def test_function7(self):
        self.assertEqual(main.function7(main.originalList.copy()), [17, 38])

    def test_function8(self):
        self.assertEqual(main.function8(main.originalList.copy()), [10, 25, 72])

    def test_function9(self):
        self.assertEqual(main.function9(main.originalList.copy()), [17, 38, 10, 25, 72])

    def test_function10(self):
        self.assertEqual(main.function10(main.originalList.copy()), 72)

if __name__ == '__main__':
    unittest.main()
