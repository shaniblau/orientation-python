import csv

from extract.csv_config import path as p
from extract.extract import Extract


class CSVExtract(Extract):

    @staticmethod
    def extract(path: str = p) -> list:
        data: list = []
        try:
            with open(path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            raise FileNotFoundError
        return data


csv_extract = CSVExtract.extract

