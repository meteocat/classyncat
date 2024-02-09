"""Module to test Classyncat circulation pattern classification."""
import unittest

from classyncat.classyncat import classyncat


class TestClassyncat(unittest.TestCase):
    """Class to test Classyncat classification"""
    def test_classyncat(self):
        """Test Classyncat classification"""
        cc_type = classyncat("A", "E")
        self.assertEqual(cc_type, 'TIP13')

        cc_type = classyncat("C", "E")
        self.assertEqual(cc_type, 'TIP12')

        cc_type = classyncat("C", "W")
        self.assertEqual(cc_type, 'TIP12')

        cc_type = classyncat("S", "C")
        self.assertEqual(cc_type, 'TIP08')

        cc_type = classyncat("S", "A")
        self.assertEqual(cc_type, 'TIP08')

        cc_type = classyncat("U", "C")
        self.assertEqual(cc_type, 'TIP10')

        cc_type = classyncat("U", "CS")
        self.assertEqual(cc_type, 'TIP09')

        cc_type = classyncat("A", "C")
        self.assertEqual(cc_type, 'TIP13')

        cc_type = classyncat("A", "CSW")
        self.assertEqual(cc_type, 'TIP02')

        cc_type = classyncat("A", "CSE")
        self.assertEqual(cc_type, 'TIP13')

        cc_type = classyncat("A", "A")
        self.assertEqual(cc_type, 'TIP13')

        cc_type = classyncat("A", "ASW")
        self.assertEqual(cc_type, 'TIP02')

        cc_type = classyncat("A", "ASE")
        self.assertEqual(cc_type, 'TIP13')

        cc_type = classyncat("A", "SW")
        self.assertEqual(cc_type, 'TIP02')

        cc_type = classyncat("A", "SE")
        self.assertEqual(cc_type, 'TIP13')

        cc_type = classyncat("AE", "C")
        self.assertEqual(cc_type, 'TIP07')

        cc_type = classyncat("AE", "A")
        self.assertEqual(cc_type, 'TIP06')

        cc_type = classyncat("AS", "AS")
        self.assertEqual(cc_type, 'TIP08')

        cc_type = classyncat("ASW", "ASW")
        self.assertEqual(cc_type, 'TIP09')

        cc_type = classyncat("AW", "AW")
        self.assertEqual(cc_type, 'TIP02')

        cc_type = classyncat("ANW", "ANW")
        self.assertEqual(cc_type, 'TIP03')

        cc_type = classyncat("AN", "AN")
        self.assertEqual(cc_type, 'TIP04')

        cc_type = classyncat("ANE", "ANE")
        self.assertEqual(cc_type, 'TIP05')

        cc_type = classyncat("C", "C")
        self.assertEqual(cc_type, 'TIP11')

        cc_type = classyncat("C", "A")
        self.assertEqual(cc_type, 'TIP12')

        cc_type = classyncat("C", "ANW")
        self.assertEqual(cc_type, 'TIP11')

        cc_type = classyncat("C", "U")
        self.assertEqual(cc_type, 'TIP12')

        cc_type = classyncat("C", "N")
        self.assertEqual(cc_type, 'TIP11')

        cc_type = classyncat("CE", "C")
        self.assertEqual(cc_type, 'TIP07')

        cc_type = classyncat("CE", "N")
        self.assertEqual(cc_type, 'TIP06')

        cc_type = classyncat("CS", "N")
        self.assertEqual(cc_type, 'TIP08')

        cc_type = classyncat("CSW", "N")
        self.assertEqual(cc_type, 'TIP09')

        cc_type = classyncat("CW", "C")
        self.assertEqual(cc_type, 'TIP10')

        cc_type = classyncat("CW", "N")
        self.assertEqual(cc_type, 'TIP01')

        cc_type = classyncat("CNW", "C")
        self.assertEqual(cc_type, 'TIP03')

        cc_type = classyncat("CN", "C")
        self.assertEqual(cc_type, 'TIP04')

        cc_type = classyncat("CNE", "C")
        self.assertEqual(cc_type, 'TIP05')

        cc_type = classyncat("E", "C")
        self.assertEqual(cc_type, 'TIP07')

        cc_type = classyncat("E", "NE")
        self.assertEqual(cc_type, 'TIP06')

        cc_type = classyncat("CW", "C")
        self.assertEqual(cc_type, 'TIP10')

        cc_type = classyncat("SW", "S")
        self.assertEqual(cc_type, 'TIP09')

        cc_type = classyncat("S", "C")
        self.assertEqual(cc_type, 'TIP08')

        cc_type = classyncat("SW", "C")
        self.assertEqual(cc_type, 'TIP09')

        cc_type = classyncat("W", "C")
        self.assertEqual(cc_type, 'TIP01')

        cc_type = classyncat("NW", "C")
        self.assertEqual(cc_type, 'TIP03')

        cc_type = classyncat("N", "C")
        self.assertEqual(cc_type, 'TIP04')

        cc_type = classyncat("NE", "C")
        self.assertEqual(cc_type, 'TIP05')

        cc_type = classyncat("U", "CS")
        self.assertEqual(cc_type, 'TIP09')

        cc_type = classyncat("U", "CNW")
        self.assertEqual(cc_type, 'TIP10')

        cc_type = classyncat("U", "A")
        self.assertEqual(cc_type, 'TIP12')
