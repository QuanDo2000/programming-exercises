# ID: 016
# Name: Power Digit Sum
# Description: 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#              What is the sum of the digits of the number 2^1000?
# Link: https://projecteuler.net/problem=16
# Help:


import sys  # Import exit()


# Function power_digit_sum():
#   Calculates the digit sum of a base raised to a power
def power_digit_sum(base, exp):
    return sum([int(i) for i in str(pow(base, exp))])


# Check number input
try:
    base = int(input("Enter base: "))
    exp = int(input("Enter exponent: "))
except ValueError:
    # Handle input error
    print("Invalid Input.\nExit...")
    sys.exit()
print("The digit sum is: {}".format(power_digit_sum(base, exp)))
