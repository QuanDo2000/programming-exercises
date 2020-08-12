# ID: 014
# Name: Longest Collatz sequence
# Description: The following iterative sequence is defined for the set of
#              positive integers:
#              n → n/2 (n is even)
#              n → 3n + 1 (n is odd)
#              Using the rule above and starting with 13, we generate the
#              following sequence:
#              13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#              It can be seen that this sequence (starting at 13 and finishing
#              at 1) contains 10 terms. Although it has not been proved yet
#              (Collatz Problem), it is thought that all starting numbers
#              finish at 1.
#              Which starting number, under one million, produces the longest
#              chain?
#              NOTE: Once the chain starts the terms are allowed to go above
#              one million.
# Link: https://projecteuler.net/problem=14
# Help: 014_overview.pdf from https://projecteuler.net/problem=14


import sys  # Import exit()


# Dict storing already calculated lengths
values = {1: 1}


# Function len_collatz_gen():
#   Output the lengths of the Collatz sequence of num
def len_collatz_gen(num):
    try:
        return(values[num])
    except:
        if (num % 2 == 0):
            values[num] = 1 + len_collatz_gen(int(num/2))
        else:
            values[num] = 2 + len_collatz_gen(int((3*num + 1)/2))
        return values[num]


# Function longest_chain():
#   Get longest chain from limit to limit / 2
def longest_chain(limit):
    longest = 0
    ans = -1
    for i in range(limit, int(limit/2)-1, -1):
        if len_collatz_gen(i) > longest:
            longest = len_collatz_gen(i)
            ans = i
    return ans


# Check number input
try:
    limit = int(input("Enter limit: "))
except ValueError:
    # Handle input error
    print("Invalid Input.\nExit...")
    sys.exit()
# Output
print("Calculating...")
print("The starting number with the longest chain is: {}".format(longest_chain(limit)))
