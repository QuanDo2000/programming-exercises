"""
ID: 13
Name: Large sum
Description:
    Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
    37107287533902102798797998220837590246510135740250
    46376937677490009712648124896970078050417018260538
    ...
    20849603980134001723930671666823555245252804609722
    53503534226472524250874054075591789781264330331690
Link: https://projecteuler.net/problem=13
"""


import sys
import os
import inspect


def read_file(filename):
    """Parse input file."""
    array = []
    path = os.path.dirname(os.path.abspath(
        inspect.getfile(inspect.currentframe()))) + "/data/" + filename
    with open(path, "r") as f:
        for line in f:
            array = array + [int(line)]
    return array


# Check number input
try:
    num = int(input("Enter amount of numbers: "))
except ValueError:
    # Handle input error
    print("Invalid Input.\nExit...")
    sys.exit()

value = sum(read_file("euler_inp_13.txt"))
value = str(value)
print("The first {} digits of the sum is {}".format(num, value[:num]))