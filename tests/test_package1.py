import unittest

from package1 import action


class TestPackag1(unittest.TestCase):

    def test_add_integers(self):
        result = action.add(1, 2)
        self.assertEqual(result, 3)

    def test_minus_integers(self):
        result = action.minus(1, 2)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
