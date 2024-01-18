import unittest

from utils.centre_graella import calcula_centre_graella


class TestClassyncat(unittest.TestCase):

    def test_classyncat(self):
        punts1 = 'tests/data/list_points_mslp'

        cenlat = calcula_centre_graella(punts1)
        self.assertEqual(cenlat, 40.0)
