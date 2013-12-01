"""Unit tests for CaBi models
"""

import unittest
import datetime
import pycabi


class TestModels(unittest.TestCase):
    def test_get_system_status_local(self):
        cabi = pycabi.get_system_status("tests/bikeStations.xml")
        self.assertEqual(len(cabi), 300)
        self.assertEqual(
            cabi["31000"].install_date,
            datetime.datetime(2011, 9, 15, 0, 0, 0)
        )

    def test_get_system_status_web(self):
        cabi = pycabi.get_system_status()
        self.assertGreater(len(cabi), 0)


if __name__ == '__main__':
    unittest.main()
