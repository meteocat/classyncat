import unittest
import numpy as np

from classyncat.jenkinson_collison_500 import jenkinson_collison_500


class TestJenkinson500(unittest.TestCase):
    center = 40.0

    def test_jenkinson_collison_500_pure_types(self):
        grib_data = np.array(
            [[57000, 57000, 57000], [52000, 52000, 52000], [47000, 47000, 47000]]
        )

        jc_type = jenkinson_collison_500(
            {"2012-01-01": grib_data.flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["E"])

        jc_type = jenkinson_collison_500(
            {"2012-01-01": np.rot90(grib_data).flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["N"])

        jc_type = jenkinson_collison_500(
            {"2012-01-01": np.rot90(grib_data, 2).flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["W"])

        jc_type = jenkinson_collison_500(
            {"2012-01-01": np.rot90(grib_data, 3).flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["S"])

        grib_data = np.array(
            [[47000, 47000, 47000], [47000, 57000, 47000], [47000, 47000, 47000]]
        )
        jc_type = jenkinson_collison_500(
            {"2012-01-01": grib_data.flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["A"])

        grib_data = np.array(
            [[57000, 57000, 57000], [57000, 47000, 57000], [57000, 57000, 57000]]
        )
        jc_type = jenkinson_collison_500(
            {"2012-01-01": grib_data.flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["C"])

    def test_jenkinson_collison_500_compound_types(self):
        grib_data = np.array(
            [[42000, 47000, 52000], [47000, 52000, 52000], [55000, 55000, 57000]]
        )

        # Direction
        jc_type = jenkinson_collison_500(
            {"2021-01-01": grib_data.flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["SW"])

        jc_type = jenkinson_collison_500(
            {"2021-01-01": np.rot90(grib_data).flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["SE"])

        jc_type = jenkinson_collison_500(
            {"2021-01-01": np.rot90(grib_data, 2).flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["NE"])

        jc_type = jenkinson_collison_500(
            {"2021-01-01": np.rot90(grib_data, 3).flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["NW"])

        # Cyclonic
        grib_data = np.array(
            [[57000, 57000, 57000], [55000, 47000, 55000], [47000, 47000, 47000]]
        )

        jc_type = jenkinson_collison_500(
            {"2021-01-01": grib_data.flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["CE"])

        jc_type = jenkinson_collison_500(
            {"2021-01-01": np.rot90(grib_data).flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["CN"])

        jc_type = jenkinson_collison_500(
            {"2021-01-01": np.rot90(grib_data, 2).flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["CW"])

        jc_type = jenkinson_collison_500(
            {"2021-01-01": np.rot90(grib_data, 3).flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["CS"])

        grib_data = np.array(
            [[57000, 55000, 52000], [52000, 47000, 45000], [52000, 52000, 42000]]
        )

        jc_type = jenkinson_collison_500(
            {"2021-01-01": grib_data.flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["CNE"])

        jc_type = jenkinson_collison_500(
            {"2021-01-01": np.rot90(grib_data).flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["CNW"])

        jc_type = jenkinson_collison_500(
            {"2021-01-01": np.rot90(grib_data, 2).flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["CSW"])

        jc_type = jenkinson_collison_500(
            {"2021-01-01": np.rot90(grib_data, 3).flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["CSE"])

        # Anticyclonic
        grib_data = np.array(
            [[57000, 57000, 57000], [55000, 57000, 55000], [47000, 47000, 47000]]
        )

        jc_type = jenkinson_collison_500(
            {"2021-01-01": grib_data.flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["AE"])

        jc_type = jenkinson_collison_500(
            {"2021-01-01": np.rot90(grib_data).flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["AN"])

        jc_type = jenkinson_collison_500(
            {"2021-01-01": np.rot90(grib_data, 2).flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["AW"])

        jc_type = jenkinson_collison_500(
            {"2021-01-01": np.rot90(grib_data, 3).flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["AS"])

        grib_data = np.array(
            [[57000, 52000, 57000], [52000, 57000, 52000], [42000, 52000, 57000]]
        )

        jc_type = jenkinson_collison_500(
            {"2021-01-01": grib_data.flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["ASE"])

        jc_type = jenkinson_collison_500(
            {"2021-01-01": np.rot90(grib_data).flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["ANE"])

        jc_type = jenkinson_collison_500(
            {"2021-01-01": np.rot90(grib_data, 2).flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["ANW"])

        jc_type = jenkinson_collison_500(
            {"2021-01-01": np.rot90(grib_data, 3).flatten()}, self.center
        )
        self.assertEqual(list(jc_type.values()), ["ASW"])
