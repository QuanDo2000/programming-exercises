"""
ID: 004
Name: Largest palindrome product
Description:
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.
Link: https://projecteuler.net/problem=4
Help:
- https://stackoverflow.com/questions/24772179/largest-palindrome-product-euler-project
- https://www.xarg.org/puzzle/project-euler/problem-4/
"""


import sys


def check_palindrome(string):
    """Return if string is palindrome."""
    if string == string[::-1]:
        return True
    else:
        return False


def find_palindrome(digits):
    """Return largest palindrome of product of two number in range 0 to limit (inclusive)."""
    largest = 0
    limit = (10 ** digits) - 1
    lower_lim = (10 ** (digits - 1)) - 1
    for i in range(limit - 1, lower_lim, -1):
        #  j going from limit down so if i * limit is <= largest then break
        if (largest >= i * limit):
            break
        for j in range(limit, i, -1):
            num = i * j
            # num moving from large to small so if palindrome > largest -> break
            if (check_palindrome(str(num)) and largest < num):
                largest = num
                break
    return largest


# Check input error
try:
    digits = int(input("Enter number of digits: "))
except ValueError:
    # Handle input error
    print("Invalid Input.\nExit...")
    sys.exit()

# Print result
print("\nAmount of digits: {}".format(digits))
result = find_palindrome(digits)
print("Largest Palindrome is: {}".format(result))
