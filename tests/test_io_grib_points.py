"""Module to test IO grib points.
"""
import unittest

from inout.grib_points import get_jc_grib_points


class TestIOGribPoints(unittest.TestCase):
    """Class to test IO grib points functions"""

    def test_get_jc_grib_points(self):
        """Test extract grib value for specific points"""

        grib_mslp = "tests/data/era5_slp_2022-02-01.grb"
        grib_z500 = "tests/data/era5_500_2022-02-01.grb"
        points_mslp = "tests/data/list_points_mslp"
        points_z500 = "tests/data/list_points_500mb"

        grib_points = get_jc_grib_points(grib_mslp, points_mslp, grib_z500, points_z500)

        self.assertEqual(
            list(grib_points["slp"].values())[0],
            [
                103958.5625,
                103220.5625,
                101021.3125,
                103079.5625,
                102178.5625,
                100624.3125,
                102839.0625,
                102399.5625,
                101303.8125,
            ],
        )
        self.assertEqual(
            list(grib_points["z500"].values())[0],
            [
                57784.3359375,
                56880.0859375,
                54562.5859375,
                57008.0859375,
                56712.5859375,
                55079.0859375,
                56516.8359375,
                56445.8359375,
                55412.8359375,
            ],
        )
