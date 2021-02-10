import unittest
from unittest import TestCase

from assignment2 import calculate_points, my_points_against_elmo

output_file_path = "output/output1.txt"


class Test(TestCase):
    # def test_calculate_points_given_examples(self):
    #     self.assertEqual(2, calculate_points([1, 2, 3]))
    #     self.assertEquals(7, calculate_points([5, 10, 2, 3]))
    #     self.assertEquals(0, calculate_points([100]), 0)

    def test_count_crossings(self):
        my_points_against_elmo("test_input/sample1.txt", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual("2", output_file.readline(), "Sample 1")
        my_points_against_elmo("test_input/sample2.txt", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual("7", output_file.readline(), "Sample 2")
        my_points_against_elmo("test_input/sample3.txt", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual("0", output_file.readline(), "Sample 3")


if __name__ == '__main__':
    unittest.main(verbosity=2)
