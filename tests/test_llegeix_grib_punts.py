import unittest

from inout.llegeix_grib_punts import llegeix_grib_punts


class TestClassyncat(unittest.TestCase):

    def test_classyncat(self):
        input_dir = 'tests/data/'
        punts1 = 'tests/data/list_points_mslp'
        punts2 = 'tests/data/list_points_500mb'

        grid1, grid2 = llegeix_grib_punts(input_dir, punts1, punts2)
        self.assertEqual(list(grid1.values())[0][4], 102178.5625)
        self.assertEqual(list(grid2.values())[0][4], 56712.5859375)
