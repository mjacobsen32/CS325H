import unittest
from unittest import TestCase

from assignment1 import count_crossings, array_input, check_intersect

output_file_path = "output/output1.txt"


class CrossingsTest(TestCase):
    def test_custom_tests(self):
        count_crossings("test_input/EMH1.txt", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual("2", output_file.readline(), "EMH 1")

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


class IOTest(TestCase):
    def test_array_input(self):
        self.assertEqual(["1", "2", "3"], array_input("test_input/sample1.txt", 1), "Line 1")
        self.assertEqual(["3", "2", "1"], array_input("test_input/sample1.txt", 2), "Line 2")


class Test(TestCase):
    def test_check_intersect(self):
        self.assertEqual(0, check_intersect([0, 0], [1, 1]))
        self.assertEqual(0, check_intersect([10, 22], [41, 100]))


if __name__ == '__main__':
    unittest.main(verbosity=2)
