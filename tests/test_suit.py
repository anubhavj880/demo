import unittest

from tests import test_package1


def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_package1.TestPackag1('test_add_integers'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
