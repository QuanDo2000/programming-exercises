import math
import sys

n = int(input())

sieve = [True] * (n + 1)
sieve[0] = False
sieve[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if sieve[i] == True:
        for j in range(i ** 2, n + 1, i):
            sieve[j] = False
# print(sieve)

# prime = [i for i, val in enumerate(sieve) if val]
# print(prime)

for i, val in enumerate(sieve):
    if val == True:
        if sieve[n - i] == True:
            print(i, n - i)
            sys.exit()
print(-1)
