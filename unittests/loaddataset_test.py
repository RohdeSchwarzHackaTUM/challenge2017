import unittest
from lib.dataset import record_reader
from lib.simple_dataset import SimpleDataset
from lib.record import *
import os

IMAGES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "program")

class TestLoadDataset(unittest.TestCase):
    def test_default_with_token(self):
        records = record_reader(IMAGES_PATH)
        self.assertEqual(len(records), 4)

    def test_simple_dataset(self):
        dataset = SimpleDataset(IMAGES_PATH, "brHD")
        expected = [True, True, True, False]
        i = 0
        for dat in dataset:
            self.assertEqual(dat[0], expected[i])
            i = i + 1
