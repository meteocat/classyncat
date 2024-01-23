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
