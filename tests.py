import unittest
import task


class TestCase(unittest.TestCase):
    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())


class TestArea(TestCase):
    def test_circle_area(self):
        rad = 5
        self.assertEqual(78.5, task.circleArea(rad))

        rad = 7
        self.assertEqual(153.86, task.circleArea(rad))

if __name__ == '__main__':
    unittest.main()
