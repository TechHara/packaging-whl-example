import unittest
from awesome_project import mean


class TestMean(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean.take_average([1,2,3,4,5]), 3.0)