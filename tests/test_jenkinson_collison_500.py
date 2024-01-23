"""Module to test JC z500 classification types"""
import unittest
import numpy as np

from classyncat.jenkinson_collison import jenkinson_collison_500


class TestJenkinsonCollison500(unittest.TestCase):
    """Class to test JC z500 classification types"""

    center = 40.0

    def test_jenkinson_collison_500_pure_types(self):
        """Test Jenkinson Collison z500 classification pure types"""
        grib_data = np.array(
            [[57000, 57000, 57000], [52000, 52000, 52000], [47000, 47000, 47000]]
        )

        jc_type = jenkinson_collison_500(grib_data.flatten(), self.center)
        self.assertEqual(jc_type, "E")

        jc_type = jenkinson_collison_500(np.rot90(grib_data).flatten(), self.center)
        self.assertEqual(jc_type, "N")

        jc_type = jenkinson_collison_500(np.rot90(grib_data, 2).flatten(), self.center)
        self.assertEqual(jc_type, "W")

        jc_type = jenkinson_collison_500(np.rot90(grib_data, 3).flatten(), self.center)
        self.assertEqual(jc_type, "S")

        grib_data = np.array(
            [[47000, 47000, 47000], [47000, 57000, 47000], [47000, 47000, 47000]]
        )
        jc_type = jenkinson_collison_500(grib_data.flatten(), self.center)
        self.assertEqual(jc_type, "A")

        grib_data = np.array(
            [[57000, 57000, 57000], [57000, 47000, 57000], [57000, 57000, 57000]]
        )
        jc_type = jenkinson_collison_500(grib_data.flatten(), self.center)
        self.assertEqual(jc_type, "C")

    def test_jenkinson_collison_500_compound_types(self):
        """Test Jenkinson Collison z500 classification compound types"""
        grib_data = np.array(
            [[42000, 47000, 52000], [47000, 52000, 52000], [55000, 55000, 57000]]
        )

        # Direction
        jc_type = jenkinson_collison_500(grib_data.flatten(), self.center)
        self.assertEqual(jc_type, "SW")

        jc_type = jenkinson_collison_500(np.rot90(grib_data).flatten(), self.center)
        self.assertEqual(jc_type, "SE")

        jc_type = jenkinson_collison_500(np.rot90(grib_data, 2).flatten(), self.center)
        self.assertEqual(jc_type, "NE")

        jc_type = jenkinson_collison_500(np.rot90(grib_data, 3).flatten(), self.center)
        self.assertEqual(jc_type, "NW")

        # Cyclonic
        grib_data = np.array(
            [[57000, 57000, 57000], [55000, 47000, 55000], [47000, 47000, 47000]]
        )

        jc_type = jenkinson_collison_500(grib_data.flatten(), self.center)
        self.assertEqual(jc_type, "CE")

        jc_type = jenkinson_collison_500(np.rot90(grib_data).flatten(), self.center)
        self.assertEqual(jc_type, "CN")

        jc_type = jenkinson_collison_500(np.rot90(grib_data, 2).flatten(), self.center)
        self.assertEqual(jc_type, "CW")

        jc_type = jenkinson_collison_500(np.rot90(grib_data, 3).flatten(), self.center)
        self.assertEqual(jc_type, "CS")

        grib_data = np.array(
            [[57000, 55000, 52000], [52000, 47000, 45000], [52000, 52000, 42000]]
        )

        jc_type = jenkinson_collison_500(grib_data.flatten(), self.center)
        self.assertEqual(jc_type, "CNE")

        jc_type = jenkinson_collison_500(np.rot90(grib_data).flatten(), self.center)
        self.assertEqual(jc_type, "CNW")

        jc_type = jenkinson_collison_500(np.rot90(grib_data, 2).flatten(), self.center)
        self.assertEqual(jc_type, "CSW")

        jc_type = jenkinson_collison_500(np.rot90(grib_data, 3).flatten(), self.center)
        self.assertEqual(jc_type, "CSE")

        # Anticyclonic
        grib_data = np.array(
            [[57000, 57000, 57000], [55000, 57000, 55000], [47000, 47000, 47000]]
        )

        jc_type = jenkinson_collison_500(grib_data.flatten(), self.center)
        self.assertEqual(jc_type, "AE")

        jc_type = jenkinson_collison_500(np.rot90(grib_data).flatten(), self.center)
        self.assertEqual(jc_type, "AN")

        jc_type = jenkinson_collison_500(np.rot90(grib_data, 2).flatten(), self.center)
        self.assertEqual(jc_type, "AW")

        jc_type = jenkinson_collison_500(np.rot90(grib_data, 3).flatten(), self.center)
        self.assertEqual(jc_type, "AS")

        grib_data = np.array(
            [[57000, 52000, 57000], [52000, 57000, 52000], [42000, 52000, 57000]]
        )

        jc_type = jenkinson_collison_500(grib_data.flatten(), self.center)
        self.assertEqual(jc_type, "ASE")

        jc_type = jenkinson_collison_500(np.rot90(grib_data).flatten(), self.center)
        self.assertEqual(jc_type, "ANE")

        jc_type = jenkinson_collison_500(np.rot90(grib_data, 2).flatten(), self.center)
        self.assertEqual(jc_type, "ANW")

        jc_type = jenkinson_collison_500(np.rot90(grib_data, 3).flatten(), self.center)
        self.assertEqual(jc_type, "ASW")
