import unittest
import time
from unittest import TestCase

from assignment1 import count_crossings, array_input, check_intersect, recurse_crossing, find_median_index

output_file_path = "output/output1.txt"


class CrossingsTest(TestCase):
    def test_custom_tests(self):
        count_crossings("test_input/EMH1.txt", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual("2", output_file.readline(), "EMH 1")
        count_crossings("test_input/EMH2.txt", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual("1", output_file.readline(), "EMH 2")
        count_crossings("test_input/EMH3.txt", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual("5", output_file.readline(), "EMH 3")

    def test_count_crossings(self):
        count_crossings("test_input/sample1.txt", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual("3", output_file.readline(), "Sample 1")
        count_crossings("test_input/sample2.txt", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual("3", output_file.readline(), "Sample 2")
        count_crossings("test_input/sample3.txt", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual("1", output_file.readline(), "Sample 3")

    def test_given_examples(self):
        count_crossings("given_examples/input0.txt", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual("2", output_file.readline(), "Example 0")
        count_crossings("given_examples/input1.txt", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual("0", output_file.readline(), "Example 1")
        count_crossings("given_examples/input2.txt", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual("0", output_file.readline(), "Example 2")
        count_crossings("given_examples/input3.txt", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual("1225", output_file.readline(), "Example 3")

    def test_long_example(self):
        start = time.time()
        count_crossings("given_examples/input4.txt", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual("499999500000", output_file.readline(), "Example 4")
        self.assertTrue(time.time() - start < 20)


class IOTest(TestCase):
    def test_array_input(self):
        self.assertEqual(["1", "2", "3"], array_input("test_input/sample1.txt", 1), "Line 1")
        self.assertEqual(["3", "2", "1"], array_input("test_input/sample1.txt", 2), "Line 2")


class TestBaseIntersections(TestCase):
    def test_check_intersect(self):
        self.assertEqual(0, check_intersect([0, 0], [1, 1]))
        self.assertEqual(0, check_intersect([10, 22], [41, 100]))


class TestNewCrossings(TestCase):
    def test_recurse_crossings(self):
        self.assertEqual(0, recurse_crossing([[0, 0], [1, 1]]))
        self.assertEqual(0, recurse_crossing([[10, 22], [41, 100]]))
        self.assertEqual(1, recurse_crossing([[0, 1], [1, 0]]))
        self.assertEqual(3, recurse_crossing([[1, 3], [2, 2], [3, 1]]))
        self.assertEqual(1, recurse_crossing([[10, 22], [20, 1], [30, 25], [41, 100]]))


class TestMedians(TestCase):
    def test_medians(self):
        self.assertEqual(1, find_median_index([[0, 0], [1, 0], [-1, 0]]))
        # self.assertEqual(10,
        #                  find_median_index(
        #                      [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0],
        #                       [11, 0], [12, 0], [13, 0], [14, 0], [15, 0], [16, 0], [17, 0], [18, 0], [19, 0],
        #                       [20, 0]]))


if __name__ == '__main__':
    unittest.main(verbosity=2)
