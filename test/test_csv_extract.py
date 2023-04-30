import csv
import unittest

from extract import csv_extract


class TestCSVExtract(unittest.TestCase):
    path: str = "../MadaReports - MadaReports.csv"
    data: list = csv_extract()

    def test_extract_func(self):
        self.assertNotEqual(self.data, [])

    def test_hermeticity(self):
        self.assertEqual(len(self.data), 1000)

    def test_reliability(self):
        self.assertTrue(self.check_equals(self.path))

    def check_equals(self, path):
        i = 0
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row not in self.data:
                    i += 1
                    if i > 1:
                        return False
        return True

    def test_file_not_exists(self):
        self.assertTrue(self.check_error())

    @staticmethod
    def check_error():
        try:
            csv_extract("path")
        except FileNotFoundError:
            return True
        return False
