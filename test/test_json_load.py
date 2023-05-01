data = []
for i in range(100000):
    data.append(i)
with open("../fadw", 'r') as file:
    lines = file.read()
items = lines.split("/n")[:-1]


def test_create_sub_list(json_load_fixture):
    result = json_load_fixture(data, 0, 3)
    assert result == [0, 1, 2, 3]


def test_hermeticity():
    amount = len(items)
    assert amount == 100000


def test_reliability():
    assert check_equals() == True


def check_equals():
    for item in items:
        if int(item) not in data:
            return False
    return True
