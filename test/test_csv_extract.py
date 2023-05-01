import csv


def check_equals(csv_extract_fixture, path: str = "../MadaReports - MadaReports.csv"):
    i = 0
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row not in csv_extract_fixture:
                i += 1
                if i > 1:
                    return False
    return True


def test_extract_func(csv_extract_fixture):
    assert csv_extract_fixture != []


def test_hermeticity(csv_extract_fixture):
    assert len(csv_extract_fixture) == 1000


def test_reliability(csv_extract_fixture):
    assert check_equals(csv_extract_fixture) == True

