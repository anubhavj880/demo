"""
This module has one method
1. pow_avg
"""
from package2 import expo
from package2.subpackage2_1 import stat

"""
@pow_avg This method is used for raise power to average of first two number
"""
def pow_avg(a, b, c):
    """
    :param a: first integer number
    :param b: second integer number
    :param c: third integer number
    :return:  return average of first and second number raise to third number
    """
    temp = stat.average(a, b)
    return expo.power(temp, c)
