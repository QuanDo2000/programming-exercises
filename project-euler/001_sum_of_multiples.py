# ID: 001
# Name: Multiples of 3 and 5
# Description: If we list all the natural numbers below 10 that are multiples
#              of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is
#              23. Find the sum of all the multiples of 3 or 5 below 1000.
# Link: https://projecteuler.net/problem=1
# Help:
#   https://math.stackexchange.com/questions/9259/find-the-sum-of-all-the-multiples-of-3-or-5-below-1000


import sys   # Import exit()
import math  # Import gcd()


# Function sum_of_multiples:
#   Find the sum of all the multiples of a number below an upper_bound
#   (not inclusive)
def sum_of_multiples(upper_bound, number):
    n = (upper_bound-1) // number
    return (number * 1/2 * n * (n + 1))


# Function lcm:
#   Find the lowest common multiple of a and b
def lcm(a, b):
    return (a * b) // math.gcd(a, b)


# Function sum_of_all_multiples
#   Find the sum of all the multiples of all numbers in a list of numbers
def sum_of_all_multiples(upper_bound, num_in):
    total = 0
    # Sum of all the multiples
    for i in num_in:
        total += sum_of_multiples(upper_bound, i)
    # Minus all the duplicate multiples
    for i in range(len(num_in)):
        for j in range(i+1, len(num_in)):
            total -= sum_of_multiples(upper_bound, lcm(num_in[i], num_in[j]))
    return total


# Check for input errors
try:
    upper_bound = int(input("Enter upper bound: "))
    num_in = []
    while True:
        num_in.append(int(input("Enter a number: ")))
        condition = "a"
        while condition not in ["n", "y"]:
            condition = input("Continue...(y/n) ")
        if condition == "n":
            break
        else:
            continue
except ValueError:
    # Handle invalid input
    print("Invalid Input.\nExit...")
    sys.exit()

# Print the result
print("\nUpper Bound: {0:,}".format(upper_bound))
print("Calculating for multiples of: {0}".format(num_in))
print("The sum is: {0:,.0f}".format(sum_of_all_multiples(upper_bound, num_in)))
