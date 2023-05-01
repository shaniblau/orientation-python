import csv
from extract import csv_extract

path: str = "../MadaReports - MadaReports.csv"
data: list = csv_extract()


def check_equals(a_path):
    i = 0
    with open(a_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row not in data:
                i += 1
                if i > 1:
                    return False
    return True


def check_error():
    try:
        csv_extract("path")
    except FileNotFoundError:
        return True
    return False


def test_extract_func():
    assert data != []


def test_hermeticity():
    assert len(data) == 1000


def test_reliability():
    assert check_equals(path) == True


def test_file_not_exists():
    assert check_error() == True
