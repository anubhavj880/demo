import unittest

import tests.test_package1 as test_package1
import tests.test_package2 as test_package2


def testsuite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(test_package1.TestPackag1())
    test_suite.addTest(test_package2.TestPackag2())
    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(testsuite())
