import unittest
import numpy as np

from classyncat.jenkinson_collison_sfc import jenkinson_collison_sfc


class TestJenkinsonsfc(unittest.TestCase):

    def test_jenkinson_collison_sfc(self):
        cenlat = 40.0
        grid = {'2012-01-01': [1, 1, 1, 0, 0, 0, -1, -1, -1]}
        type = jenkinson_collison_sfc(grid, cenlat)
        self.assertEqual(list(type.values()),['U'])
