# ID: 006
# Name: Sum square difference
# Description: The sum of the squares of the first ten natural numbers is,
#              1^2 + 2^2 + ... + 10^2 = 385
#              The square of the sum of the first ten natural numbers is,
#              (1 + 2 + ... + 10)^2 = 55^2 = 3025
#              Hence the difference between the sum of the squares of the
#              first ten natural numbers and the square of the sum is
#              3025 − 385 = 2640.
#              Find the difference between the sum of the squares of the
#              first one hundred natural numbers and the square of the sum.
# Link: https://projecteuler.net/problem=6
# Help:
#   https://math.stackexchange.com/questions/1166027/prove-that-1222-cdotsn2-fracnn12n16-for-n-in-mathbbn
#   https://codereview.stackexchange.com/questions/58460/sum-of-squares-square-of-sum-difference?rq=1


import sys  # Import exit()


# Function sum_of_square()
#   Find the sum of all the square from 0 to lim
def sum_of_square(lim):
    total = (lim * (lim + 1) * (2 * lim + 1)) / 6
    return total


# Function square_of_sum()
#   Find the square of the sum from 0 to lim
def square_of_sum(lim):
    total = (lim * (lim + 1)) / 2
    return (total ** 2)


# Check input error
try:
    limit = int(input("Enter limit: "))
except ValueError:
    # Handle input error
    print("Invalid Input.\nExit...")
    sys.exit()

# Print result
print("\nThe limit is: {}".format(limit))
sum_square = sum_of_square(limit)
square_sum = square_of_sum(limit)
result = abs(sum_square - square_sum)
print("The sum of square is: {:,.0f}".format(sum_square))
print("The square of sum is: {:,.0f}".format(square_sum))
print("The difference is: {:,.0f}".format(result))
