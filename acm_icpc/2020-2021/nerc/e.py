import math


def gcd_ex(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, (old_s, old_t)


n = int(input())
for _ in range(n):
    b, d = map(int, input().split())
    gcd, (a, c) = gcd_ex(d, b)
    rhs = (b ** 2) // gcd
    b //= gcd
    d //= gcd
    if (rhs % (b * d) == 0):
        print(rhs // (b * d) - 1)
    else:
        print(rhs // (b * d))
