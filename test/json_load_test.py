from load import JsonLoad


class JsonLoadTest():
    data = []
    for i in range(100000):
        data.append(i)
    with open("../fadw", 'r') as file:
        lines = file.read()
    items = lines.split("/n")[:-1]

    def test_create_sub_list_func(self):
        result = JsonLoad.create_sub_list(self.data, 0, 3)
        assert result == [0, 1, 2, 3]

    def test_hermeticity(self):
        amount = len(self.items)
        assert amount == 100000

    def test_reliability(self):
        assert self.check_equals() == True

    def check_equals(self):
        for item in self.items:
            if int(item) not in self.data:
                return False
        return True


