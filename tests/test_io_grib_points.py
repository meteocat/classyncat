"""Module to test IO grib points.
"""

import unittest

from classyncat.io.grib_points import get_jc_grib_points


class TestIOGribPoints(unittest.TestCase):
    """Class to test IO grib points functions"""

    grib_mslp = "tests/data/era5_slp_2022-02-01.grb"
    grib_z500 = "tests/data/era5_500_2022-02-01.grb"

    points_mslp = [
        [45.0, -10.0],
        [45.0, 0.0],
        [45.0, 10.0],
        [40.0, -10.0],
        [40.0, 0.0],
        [40.0, 10.0],
        [35.0, -10.0],
        [35.0, 0.0],
        [35.0, 10.0],
    ]

    points_z500 = [
        [45.0, -15.0],
        [45.0, -5.0],
        [45.0, 5.0],
        [40.0, -15.0],
        [40.0, -5.0],
        [40.0, 5.0],
        [35.0, -15.0],
        [35.0, -5.0],
        [35.0, 5.0],
    ]

    def test_get_jc_grib_points(self):
        """Test extract grib value for specific points"""

        grib_mslp, grib_z500 = get_jc_grib_points(
            self.grib_mslp, self.points_mslp, self.grib_z500, self.points_z500
        )

        self.assertEqual(
            list(grib_mslp.values())[0],
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
            list(grib_z500.values())[0],
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

    def test_get_jc_grib_points_wrong_type(self):
        """Test correct type for grib data/file"""
        with self.assertRaises(ValueError) as err:
            get_jc_grib_points([], self.points_mslp, self.grib_z500, self.points_z500)

        self.assertEqual(
            err.exception.args[0],
            "`grib_mslp` must be the string path to a grib file or and xarray.Dataset.",
        )

        with self.assertRaises(ValueError) as err:
            get_jc_grib_points(self.grib_mslp, self.points_mslp, [], self.points_z500)

        self.assertEqual(
            err.exception.args[0],
            "`grib_z500` must be the string path to a grib file or and xarray.Dataset.",
        )
