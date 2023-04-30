import unittest

from load import JsonLoad


class JsonLoadTest(unittest.TestCase):
    data = []
    for i in range(100000):
        data.append(i)
    with open("../fadw", 'r') as file:
        lines = file.read()
    items = lines.split("/n")[:-1]

    def test_create_sub_list_func(self):
        self.assertEqual(JsonLoad.create_sub_list(self.data, 0, 3), [0, 1, 2, 3])

    def test_hermeticity(self):
        amount = len(self.items)
        self.assertEqual(amount, 100000)

    def test_reliability(self):
        self.assertTrue(self.check_equals())

    def check_equals(self):
        for item in self.items:
            if int(item) not in self.data:
                return False
        return True


