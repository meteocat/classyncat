"""Module to test JC surface classification"""
import unittest

import numpy as np

from classyncat.jenkinson_collison import jenkinson_collison_sfc


class TestJenkinsonCollisonSfc(unittest.TestCase):
    """Class to test JC surface classification"""

    lat_0 = 40.0

    def test_jenkinson_collison_sfc_pure_types(self):
        """Test Jenkinson Collison surface classification pure types"""
        grib_data = np.array(
            [[103900, 103900, 103900], [100800, 100800, 100800], [98000, 98000, 98000]]
        )

        jc_type = jenkinson_collison_sfc(grib_data.flatten(), self.lat_0)
        self.assertEqual(jc_type, "E")

        jc_type = jenkinson_collison_sfc(np.rot90(grib_data).flatten(), self.lat_0)
        self.assertEqual(jc_type, "N")

        jc_type = jenkinson_collison_sfc(np.rot90(grib_data, 2).flatten(), self.lat_0)
        self.assertEqual(jc_type, "W")

        jc_type = jenkinson_collison_sfc(np.rot90(grib_data, 3).flatten(), self.lat_0)
        self.assertEqual(jc_type, "S")

        grib_data = np.array(
            [[98000, 98000, 98000], [98000, 1039000, 98000], [98000, 98000, 98000]]
        )
        jc_type = jenkinson_collison_sfc(grib_data.flatten(), self.lat_0)
        self.assertEqual(jc_type, "A")

        grib_data = np.array(
            [
                [103900, 103900, 103900],
                [103900, 98000, 103900],
                [103900, 103900, 103900],
            ]
        )
        jc_type = jenkinson_collison_sfc(grib_data.flatten(), self.lat_0)
        self.assertEqual(jc_type, "C")

        grib_data = np.array(
            [
                [103900, 103900, 103900],
                [103900, 103900, 103900],
                [103900, 103900, 103900],
            ]
        )
        jc_type = jenkinson_collison_sfc(grib_data.flatten(), self.lat_0)
        self.assertEqual(jc_type, "U")

    def test_jenkinson_collison_sfc_compound_types(self):
        """Test Jenkinson Collison surface classification compound types"""
        grib_data = np.array(
            [[97000, 98000, 100800], [98000, 100800, 100800], [101800, 101800, 103900]]
        )

        # Direction
        jc_type = jenkinson_collison_sfc(grib_data.flatten(), self.lat_0)
        self.assertEqual(jc_type, "SW")

        jc_type = jenkinson_collison_sfc(np.rot90(grib_data).flatten(), self.lat_0)
        self.assertEqual(jc_type, "SE")

        jc_type = jenkinson_collison_sfc(np.rot90(grib_data, 2).flatten(), self.lat_0)
        self.assertEqual(jc_type, "NE")

        jc_type = jenkinson_collison_sfc(np.rot90(grib_data, 3).flatten(), self.lat_0)
        self.assertEqual(jc_type, "NW")

        # Cyclonic CS/CW
        grib_data = np.array(
            [[103900, 103900, 103900], [101800, 98000, 101800], [97000, 97000, 97000]]
        )

        jc_type = jenkinson_collison_sfc(grib_data.flatten(), self.lat_0)
        self.assertEqual(jc_type, "CE")

        jc_type = jenkinson_collison_sfc(np.rot90(grib_data, 2).flatten(), self.lat_0)
        self.assertEqual(jc_type, "CW")

        # Cyclonic CN/CS
        grib_data = np.array(
            [[103900, 101800, 85000], [103900, 95000, 85000], [103900, 101800, 85000]]
        )

        jc_type = jenkinson_collison_sfc(grib_data.flatten(), self.lat_0)
        self.assertEqual(jc_type, "CN")

        jc_type = jenkinson_collison_sfc(np.rot90(grib_data, 2).flatten(), self.lat_0)
        self.assertEqual(jc_type, "CS")

        # Cyclonic CNE/CNW/CSW/CSE
        grib_data = np.array(
            [[103900, 101800, 100800], [101800, 98000, 95000], [100800, 95000, 93000]]
        )

        jc_type = jenkinson_collison_sfc(grib_data.flatten(), self.lat_0)
        self.assertEqual(jc_type, "CNE")

        jc_type = jenkinson_collison_sfc(np.rot90(grib_data).flatten(), self.lat_0)
        self.assertEqual(jc_type, "CNW")

        jc_type = jenkinson_collison_sfc(np.rot90(grib_data, 2).flatten(), self.lat_0)
        self.assertEqual(jc_type, "CSW")

        jc_type = jenkinson_collison_sfc(np.rot90(grib_data, 3).flatten(), self.lat_0)
        self.assertEqual(jc_type, "CSE")

        # Anticyclonic AE/AW
        grib_data = np.array(
            [[103900, 103900, 103900], [101800, 101800, 101800], [97000, 97000, 97000]]
        )

        jc_type = jenkinson_collison_sfc(grib_data.flatten(), self.lat_0)
        self.assertEqual(jc_type, "AE")

        jc_type = jenkinson_collison_sfc(np.rot90(grib_data, 2).flatten(), self.lat_0)
        self.assertEqual(jc_type, "AW")

        # Anticyclonic AN/AS
        grib_data = np.array(
            [[103900, 101800, 97000], [103900, 102800, 97000], [103900, 101800, 97000]]
        )

        jc_type = jenkinson_collison_sfc(grib_data.flatten(), self.lat_0)
        self.assertEqual(jc_type, "AN")

        jc_type = jenkinson_collison_sfc(np.rot90(grib_data, 2).flatten(), self.lat_0)
        self.assertEqual(jc_type, "AS")

        # Anticyclonic ANE/ANW/ASE/ASW
        grib_data = np.array(
            [[103900, 101800, 100800], [101800, 102000, 95000], [100800, 95000, 93000]]
        )

        jc_type = jenkinson_collison_sfc(grib_data.flatten(), self.lat_0)
        self.assertEqual(jc_type, "ANE")

        jc_type = jenkinson_collison_sfc(np.rot90(grib_data).flatten(), self.lat_0)
        self.assertEqual(jc_type, "ANW")

        jc_type = jenkinson_collison_sfc(np.rot90(grib_data, 2).flatten(), self.lat_0)
        self.assertEqual(jc_type, "ASW")

        jc_type = jenkinson_collison_sfc(np.rot90(grib_data, 3).flatten(), self.lat_0)
        self.assertEqual(jc_type, "ASE")
