import json
import os

from datetime import datetime
from .json_config import limit, directory
from .load import Load


class JsonLoad(Load):
    @staticmethod
    def load(data: list):
        if not os.path.exists(directory):
            os.mkdir(directory)
        length: int = int(len(data) / limit) + 1
        start: int = 0
        end: int = len(data) if length == 1 else limit
        for i in range(length):
            path: str = f'{directory}/{datetime.now()}.json'
            JsonLoad.load_to_limit(path, JsonLoad.create_sub_list(data, start, end))
            start = end
            end += limit

    @staticmethod
    def create_sub_list(data: list, start: int, end: int):
        i: int = 0
        sub_list: list = []
        for row in data:
            if start <= i <= end:
                sub_list.append(row)
                i += 1
        return sub_list

    @staticmethod
    def load_to_limit(path, data):
        with open(path, 'a') as file:
            json.dump(data, file)


json_load = JsonLoad.load
