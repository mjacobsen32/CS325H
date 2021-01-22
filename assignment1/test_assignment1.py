from unittest import TestCase

from assignment1 import count_crossings, array_input


class CrossingsTest(TestCase):
    def test_count_crossings(self):
        output_file_path = "output/output1.txt"
        count_crossings("test_input/sample1.txt", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual(output_file.readline(), "3")
        count_crossings("test_input/sample2.txt", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual(output_file.readline(), "3")
        count_crossings("test_input/sample2.txt", output_file_path)
        with open(output_file_path, "r") as output_file:
            self.assertEqual(output_file.readline(), "1")


class IOTest(TestCase):
    def test_array_input(self):
        self.assertEqual(array_input("test_input/sample1.txt", 1), ["1", "2", "3"])
        self.assertEqual(array_input("test_input/sample1.txt", 2), ["3", "2", "1"])
