"""
ID: 010
Name: Summation of primes
Description:
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
Link: https://projecteuler.net/problem=10
Help:
- https://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python
- https://stackoverflow.com/questions/2897297/speed-up-bitstring-bit-operations-in-python
"""


import sys


def prime_sieve(limit):
    """When used in a for loop, will print all prime upto limit."""
    a = [True] * limit
    a[0] = a[1] = False
    for (i, num) in enumerate(a):
        if num:
            yield i
            for n in range(i * i, limit, i):
                a[n] = False


# Check input error
try:
    limit = int(input("Enter limit: "))
except ValueError:
    # Handle input error
    print("Invalid Input.\nExit...")
    sys.exit()
total = 0
# Create file to write primes (Delete comments to write to file)
# path = "./output/010_prime/010_prime" + str(limit) + ".txt"
# f = open(path, "w")
for i in prime_sieve(limit):
    total += i
#     print(i, file=f)
# f.close()

# Print result
print("\nThe limit is: {}".format(limit))
print("The total is: {}".format(total))
