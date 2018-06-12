import unittest

import tests.test_package1 as test_package1
import tests.test_package2 as test_package2


def testsuite():
    test_suite = unittest.TestSuite()
    result = unittest.TestResult()
    test_suite.addTest(test_package1.TestPackag1('test_add_integers'))
    test_suite.addTest(test_package1.TestPackag1('test_minus_integers'))
    test_suite.addTest(test_package2.TestPackag2('test_power_integers'))
    test_suite.addTest(test_package2.TestPackag2('test_avg_integers'))
    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(testsuite())
