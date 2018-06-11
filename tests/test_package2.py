import unittest
from statistics import mean

from package1.subpackage1_1 import num
from package2 import expo
from package2.subpackage2_1 import stat


class TestPackag1(unittest.TestCase):
    a = 0
    b = 0

    def setUp(self):
        global a, b
        a = num.give_number()
        b = num.give_number()

    def test_power_integers(self):
        global a, b
        result = expo.power(a, b)
        self.assertEqual(result, a ** b)

    def test_avg_integers(self):
        global a, b
        result = stat.average(a, b)
        self.assertEqual(result, mean([a, b]))

    def tearDown(self):
        global a
        global b
        a = 0
        b = 0


if __name__ == '__main__':
    unittest.main()
