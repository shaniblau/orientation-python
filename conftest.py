import pytest

import extract
import load


@pytest.fixture
def json_load_fixture():
    return load.JsonLoad.create_sub_list


@pytest.fixture
def csv_extract_fixture():
    return extract.csv_extract


@pytest.fixture
def fake_file_fixture():
    with open("../fadw", 'r') as file:
        lines = file.read()
    items = lines.split("/n")[:-1]
    return items
