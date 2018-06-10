from package2 import expo
from package2.subpackage2_1 import stat


def pow_avg(a, b, c):
    temp = stat.average(a, b)
    return expo.power(temp, c)
