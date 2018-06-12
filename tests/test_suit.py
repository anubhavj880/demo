import unittest

from tests import test_package1


def suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(test_package1.TestPackag1())

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
