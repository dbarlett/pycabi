"""Unit tests for CaBi utilities
"""

import unittest
import datetime
import pycabi


class TestUtils(unittest.TestCase):
    def test_timestamp_string(self):
        self.assertEqual(
            pycabi.utils.parse_timestamp("1384650901929"),
            datetime.datetime(2013, 11, 16, 20, 15, 1, 929000)
        )

    def test_timestamp_int(self):
        self.assertEqual(
            pycabi.utils.parse_timestamp(1384650901929),
            datetime.datetime(2013, 11, 16, 20, 15, 1, 929000)
        )

    def test_duration_long_format(self):
        self.assertEqual(
            pycabi.utils.parse_trip_duration("14h 26min. 2sec"),
            51962
        )

    def test_duration_short_format(self):
        self.assertEqual(
            pycabi.utils.parse_trip_duration("14h 26m 2s"),
            51962
        )

if __name__ == '__main__':
    unittest.main()
