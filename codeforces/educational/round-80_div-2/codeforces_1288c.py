import math
mod = 10**9 + 7


def C(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


n, m = map(int, input().split())
print(C(n + 2*m - 1, 2*m) % mod)