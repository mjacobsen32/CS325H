import unittest
from unittest import TestCase

from assignment3 import minimum_cost_connecting_edges

output_file_path = "output.txt"


class CrossingsTest(TestCase):
    def test_given_examples(self):
        minimum_cost_connecting_edges("input0.in", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual("2", output_file.readline(), "Example 0")
        minimum_cost_connecting_edges("input1.txt", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual("2", output_file.readline(), "Example 1")
        minimum_cost_connecting_edges("input2.txt", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual("8", output_file.readline(), "Example 2")
        minimum_cost_connecting_edges("input3.txt", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual("10", output_file.readline(), "Example 3")
        minimum_cost_connecting_edges("input4.txt", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual("20", output_file.readline(), "Example 4")
        minimum_cost_connecting_edges("input16.in", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual("25974", output_file.readline(), "Example 16")


if __name__ == '__main__':
    unittest.main(verbosity=2)
