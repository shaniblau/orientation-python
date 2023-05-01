import csv
from extract import csv_extract


class CSVExtractTest:
    path: str = "../MadaReports - MadaReports.csv"
    data: list = csv_extract()

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

    @staticmethod
    def check_error():
        try:
            csv_extract("path")
        except FileNotFoundError:
            return True
        return False


cet = CSVExtractTest()


def test_extract_func():
    assert cet.data != []


def test_hermeticity():
    assert len(cet.data) == 1000


def test_reliability():
    assert cet.check_equals(cet.path) == True


def test_file_not_exists():
    assert cet.check_error() == True
