# ID: 015
# Name: Lattice Paths
# Description: Starting in the top left corner of a 2×2 grid, and only being
#              able to move to the right and down, there are exactly 6 routes
#              to the bottom right corner.
#              How many such routes are there through a 20×20 grid?
# Link: https://projecteuler.net/problem=15
# Help:
#   https://en.wikipedia.org/wiki/Lattice_path

import sys  # Import exit()


# Function factorial():
#   Calculates the equivalent of n! (factorial of number n)
def factorial(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret


# Function binomial_coefficient():
#   Calculates the equivalent of nCk
def binomial_coefficient(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))


# Function lattic_paths():
#   Take in size of grid and output the amount of paths to traverse the grid.
def lattic_paths(size):
    return binomial_coefficient(2*size, size)


# Check number input
try:
    size = int(input("Enter size of grid: "))
except ValueError:
    # Handle input error
    print("Invalid Input.\nExit...")
    sys.exit()
# Output
print("Amount of paths is: {:,.0f}".format(lattic_paths(size)))
