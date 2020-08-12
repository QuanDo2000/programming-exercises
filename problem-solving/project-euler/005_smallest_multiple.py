# ID: 005
# Name: Smallest multiple
# Description: 2520 is the smallest number that can be divided by each of the
#              numbers from 1 to 10 without any remainder. What is the
#              smallest positive number that is evenly divisible by all of
#              the numbers from 1 to 20?
# Link: https://projecteuler.net/problem=5
# Help:
#   https://codereview.stackexchange.com/questions/75092/project-euler-5-lowest-common-multiple-of-1-through-20?noredirect=1&lq=1


import math  # Import gcd()
import sys   # Import exit()


# Function smallest_multiple()
#   Find smallest multiple from 1 to number by multiplying the LCM of 1 to number
def smallest_multiple(number):
    num = 1
    for i in range(1, number+1):
        # Find the LCM of num and i
        num = (num * i) // (math.gcd(num, i))
    return num


# Check input error
try:
    num_in = int(input("Enter number: "))
except ValueError:
    # Handle input error
    print("Invalid Input.\nExit...")
    sys.exit()

# Print result
print("\nFinding smallest multiple of 1 to {}".format(num_in))
print("The smallest multiple is: {:,}".format(smallest_multiple(num_in)))
