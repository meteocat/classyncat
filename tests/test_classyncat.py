import unittest
import numpy as np

from classyncat.classyncat import classyncat


class TestClassyncat(unittest.TestCase):

    def test_classyncat(self):
        tipus_sfc = {'2012-01-01': 'U'}
        tipus_500 = {'2012-01-01': 'C'}

        type = classyncat(tipus_sfc, tipus_500)
        print(type)
        self.assertEqual(list(type.values()),['TIP10'])
