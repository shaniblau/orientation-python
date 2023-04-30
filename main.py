from extract import csv_extract
from load import json_load


def main():
    json_load(csv_extract())


if __name__ == '__main__':
    main()
