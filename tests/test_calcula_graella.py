import unittest

from utils.calcula_graella import calcula_graella


class TestClassyncat(unittest.TestCase):

    def test_classyncat(self):
        punts1 = 'tests/data/list_points_mslp'

        cenlat, area = calcula_graella(punts1)
        self.assertEqual(cenlat, 40.0)
        self.assertEqual(area[0], 45.0)
        self.assertEqual(area[1], -10.0)
        self.assertEqual(area[2], 35.0)
        self.assertEqual(area[3], 10.0)
