import os.path
import unittest


class Sanity(unittest.TestCase):
    def test_sanity(self):
        self.assertTrue(os.path.exists("/Users/shaniblau/Documents/pythonProjects/new/mada_reports"))
        self.assertTrue(os.path.isdir("/Users/shaniblau/Documents/pythonProjects/new/mada_reports"))
        self.assertTrue(len(os.listdir("/Users/shaniblau/Documents/pythonProjects/new/mada_reports")) >= 1)




