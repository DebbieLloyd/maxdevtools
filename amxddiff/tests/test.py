# Tests if the content of the test scripts is equal to the result of the conversion scripts.
# If not, displays the diff between the two.

import sys
import unittest
import difflib

import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

import amxd_textconv
import maxpat_textconv
import als_textconv


class TestStringMethods(unittest.TestCase):
    def test_parse_device(self):
        self.maxDiff = None

        expected_file_path = get_test_path_file("test_baselines/EncryptedTest.amxd.txt")
        test_file_path = get_test_path_file("test_files/EncryptedTest.amxd")

        with open(expected_file_path, mode="r") as expected_file:
            expected = expected_file.read()
            actual = parse(test_file_path)
            self.assertEqual(expected, actual)

    def test_parse_encrypted_device(self):
        self.maxDiff = None

        expected_file_path = get_test_path_file("test_baselines/Test.amxd.txt")
        test_file_path = get_test_path_file("test_files/Test.amxd")

        with open(expected_file_path, mode="r") as expected_file:
            expected = expected_file.read()
            actual = parse(test_file_path)
            self.assertEqual(expected, actual)

    def test_parse_maxpat(self):
        self.maxDiff = None

        expected_file_path = get_test_path_file("test_baselines/Test.maxpat.txt")
        test_file_path = get_test_path_file("test_files/Test.maxpat")

        with open(expected_file_path, mode="r") as expected_file:
            expected = expected_file.read()
            actual = parse(test_file_path)

            # print ("expected: " + expected)
            # print ("actual: " + actual)

            self.assertEqual(expected, actual)

    def test_parse_als_zipped(self):
        self.max_diff = None

        expected_file_path = get_test_path_file("test_baselines/Test.als.txt")
        test_file_path = get_test_path_file("test_files/Test Project/Test.als")

        with open(expected_file_path, mode="r") as expected_file:
            expected = expected_file.read()
            actual = parse(test_file_path)
            self.assertEqual(expected, actual)

    def test_parse_als_unzipped(self):
        self.maxDiff = None

        # result of an unzipped set should be same as a zipped set
        expected_file_path = get_test_path_file("test_baselines/Test.als.txt")
        test_file_path = get_test_path_file("test_files/Test Project/Test-NoZip.als")

        with open(expected_file_path, mode="r") as expected_file:
            expected = expected_file.read()
            actual = parse(test_file_path)
            self.assertEqual(expected, actual)


def parse(path):
    result = ""
    if path.endswith(".amxd"):
        result = amxd_textconv.parse(path)
    if path.endswith(".maxpat"):
        result = maxpat_textconv.parse(path)
    if path.endswith(".als"):
        result = als_textconv.parse(path)
    return result


def get_test_path_file(file_name):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), file_name))


if __name__ == "__main__":
    unittest.main()
