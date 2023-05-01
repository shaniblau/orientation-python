from load.json_load import JsonLoad


class JsonLoadTest:
    data = []
    for i in range(100000):
        data.append(i)
    with open("../fadw", 'r') as file:
        lines = file.read()
    items = lines.split("/n")[:-1]

    def check_equals(self):
        for item in self.items:
            if int(item) not in self.data:
                return False
        return True


jlt = JsonLoadTest()


def test_create_sub_list_func():
    result = JsonLoad.create_sub_list(jlt.data, 0, 3)
    assert result == [0, 1, 2, 3]


def test_hermeticity():
    amount = len(jlt.items)
    assert amount == 100000


def test_reliability():
    assert jlt.check_equals() == True
