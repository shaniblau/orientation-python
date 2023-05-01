import pytest

import extract
import load


@pytest.fixture(scope="class")
def json_load_fixture():
    return load.JsonLoad.create_sub_list


@pytest.fixture(scope="class")
def csv_extract_fixture():
    return extract.csv_extract
