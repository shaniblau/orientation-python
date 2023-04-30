import os.path
import unittest


class Sanity(unittest.TestCase):
    path = '/Users/shaniblau/Documents/pythonProjects/orientation-python/mada_reports'

    def test_sanity(self):
        self.assertTrue(os.path.exists(self.path))
        self.assertTrue(os.path.isdir(self.path))
        self.assertTrue(len(os.listdir(self.path)) >= 1)
