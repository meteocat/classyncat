import unittest
import numpy as np

from classyncat.jenkinson_collison_500 import jenkinson_collison_500


class TestJenkinson500(unittest.TestCase):

    def test_jenkinson_collison_500(self):
        cenlat = 40.0
        grid = {'2012-01-01': [1, 1, 1, 0, 0, 0, -1, -1, -1]}
        type = jenkinson_collison_500(grid, cenlat)
        self.assertEqual(list(type.values()),['U'])
