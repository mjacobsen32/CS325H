import unittest
from unittest import TestCase

from assignment2 import calculate_points


class Test(TestCase):
    def test_calculate_points_given_examples(self):
        self.assertEqual(2, calculate_points([1, 2, 3]))
        self.assertEquals(7, calculate_points([5, 10, 2, 3]))
        self.assertEquals(0, calculate_points([100]), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
