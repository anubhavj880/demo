import home
from package1 import action
from package1.subpackage1_1 import num
from package2.subpackage2_1 import stat

a = num.give_number()
b = num.give_number()

c = 2
print("The nuber generated are {0} and {1}".format(a, b))
print("Addition of number {0} and {1} is {2}".format(a, b, action.add(a, b)))
print("Subtraction of number {0} and {1} is {2}".format(a, b, action.minus(a, b)))
print("Average of number {0} and {1} is {2}".format(a, b, stat.average(a, b)))
print("{0} power of average of number {1} and {2} is {3}".format(c, a, b, home.pow_avg(a, b, c)))
