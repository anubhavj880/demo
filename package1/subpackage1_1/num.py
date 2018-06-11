"""
This module has one method
1. generate random number
"""

from random import randint

"""
@give_number generate a random number between 100 and 999
"""
def give_number():
    """
        :return: a integer b/w 100 and 999
    """
    return randint(100, 999)
