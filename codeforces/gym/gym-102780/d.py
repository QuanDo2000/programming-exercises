import math
from collections import defaultdict


EPS = 1e-9
MOD = 1e6 + 7
DEBUG = False


def prime_factors(x):
    primes = []
    ans = defaultdict(int)
    while x % 2 == 0:
        if 2 not in primes:
            primes.append(2)
        ans[2] += 1
        x /= 2
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        while x % i == 0:
            if i not in primes:
                primes.append(i)
            ans[i] += 1
            x /= i
    if x > 2:
        if x not in primes:
            primes.append(int(x))
        ans[x] += 1
    return primes, ans


def power(x, n):
    ans = 1
    for i in range(int(n)):
        ans *= x
        ans %= MOD
    return ans


def check(x):
    global primes, powers, a, b
    total = int((primes[0] ** x) % MOD)
    if DEBUG:
        print(x, total)
    for i in range(1, len(primes)):
        num = primes[i]
        q = int(x * powers[num] / powers[primes[0]])
        if (q - int(q)) > 0 + EPS:
            return 0
        total *= num ** q
        total %= MOD
        total = int(total)
        if DEBUG:
            print(x, total, q)
    num1, num2 = int(power(total, b)), int(power(a, total))
    if DEBUG:
        print(total, b, num1, a, num2)
    if num1 == num2:
        return total
    return 0


a, b = map(int, input().split())

primes, powers = prime_factors(a)

if DEBUG:
    print(primes, powers)

for t in range(1, 61):
    ans = check(t)
    if DEBUG:
        print(t, ans)
    if ans:
        print(ans)
        break
else:
    print(0)
