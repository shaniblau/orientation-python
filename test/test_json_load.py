data = []
for i in range(100000):
    data.append(i)


def test_create_sub_list(json_load_fixture):
    result = json_load_fixture(data, 0, 3)
    assert result == [0, 1, 2, 3]


def test_hermeticity(fake_file_fixture):
    amount = len(fake_file_fixture)
    assert amount == 100000


def test_reliability(fake_file_fixture):
    assert check_equals(fake_file_fixture) == True


def check_equals(fake_file_fixture):
    for item in fake_file_fixture:
        if int(item) not in data:
            return False
    return True
