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


class TestList(TestCase):
    def test_first_n_last_list(self):
        testLists = [1, 2, 3, 4, 5, 6]
        self.assertEqual('[1, 6]', task.firstNLastList(testLists))
        
        
class TestDaysInBetween(TestCase):
    def test_days_in_between(self):
        dateA = date(2014, 7, 2)
        dateB = date(2014, 7, 11)
        self.assertEqual(9, task.daysInBetween(dateA, dateB))


if __name__ == '__main__':
    unittest.main()
