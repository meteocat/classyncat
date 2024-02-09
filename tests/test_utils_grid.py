"""Module to test utils.grid
"""

import unittest

from classyncat.utils.grid import get_grid_from_file


class TestUtilsGrid(unittest.TestCase):
    """Class to test utils grid module"""

    def test_get_grid_from_file(self):
        """Test get grid center and extension from file points"""
        grid_points = [
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

        center, grid_extension = get_grid_from_file(grid_points)

        self.assertEqual(center, 40.0)
        self.assertEqual(grid_extension[0], 45.0)
        self.assertEqual(grid_extension[1], -10.0)
        self.assertEqual(grid_extension[2], 35.0)
        self.assertEqual(grid_extension[3], 10.0)

    def test_get_grid_from_file_wrong_format(self):
        """Test get grid center and extension from file points"""
        grid_points = [
            [45.0],
            [45.0, 0.0],
            [45.0, 10.0],
            [40.0, -10.0],
            [40.0, 0.0],
            [40.0, 10.0],
            [35.0, -10.0],
            [35.0, 0.0],
            [35.0, 10.0],
        ]

        with self.assertRaises(IndexError) as err:
            get_grid_from_file(grid_points)

        self.assertEqual(
            err.exception.args[0],
            "`grid_points` points may not be properly configured. They "
            "must be a list of latitude and longitude coordinate tuples.",
        )
