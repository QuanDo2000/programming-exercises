# ID: 007
# Name: 10001st prime
# Description: By listing the first six prime numbers:
#              2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#              What is the 10 001st prime number?
# Link: https://projecteuler.net/problem=7
# Help:
#


import sys  # Import exit()


# Function nth_prime()
# Find the nth prime number
def nth_prime(n):
    # Create prime number list up to nth number
    prime_list = [2]
    num = 3
    while len(prime_list) < n:
        # If num a multiple of a smaller prime then break
        for p in prime_list:
            if num % p == 0:
                break
        else:
            prime_list.append(num)
        # Increment num in steps of 2
        num += 2
    # Return largest prime
    return prime_list[-1]


# Check input error
try:
    index = int(input("Enter index: "))
except ValueError:
    # Handle input error
    print("Invalid Input.\nExit...")
    sys.exit()

# Print result
print("\nThe index is: {:,}".format(index))
print("The prime number is: {:,}".format(nth_prime(index)))
