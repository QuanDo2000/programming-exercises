from collections import defaultdict
import sys

sys.setrecursionlimit(int(1e6))

MOD = 1e9 + 7
EPS = 1e-9
DEBUG = True


def area(p1, p2, p3):
    (x1, y1) = p1
    (x2, y2) = p2
    (x3, y3) = p3
    return abs((x1 - x3) * (y2 - y1) - (x1 - x2) * (y3 - y1)) / 2.0


def pit(p, p1, p2, p3):
    global EPS
    a = area(p1, p2, p3)

    a1 = area(p, p2, p3)
    a2 = area(p, p1, p3)
    a3 = area(p, p1, p2)

    return abs(a - a1 - a2 - a3) < EPS


def ncr(i, j):
    global d
    if d[(i, j)] != 0:
        return d[(i, j)]
    elif d[(i, i - j)] != 0:
        return d[(i, i - j)]
    elif (i == j) or (i - j == i):
        d[(i, j)] = 1
        return 1
    else:
        ans = (ncr(i - 1, j - 1) % MOD) + (ncr(i - 1, j) % MOD) % MOD
        d[(i, j)] = ans
        return ans


t = int(input())

d = defaultdict(int)

for _ in range(t):
    xa, ya, xb, yb, xc, yc = map(int, input().split())
    p1 = (xa, ya)
    p2 = (xb, yb)
    p3 = (xc, yc)

    y_max = max(ya, yb, yc)
    x_min, x_max = min(xa, xb, xc), max(xa, xb, xc)
    ans = 0
    for i in range(y_max + 1):
        for j in range(i + 1):
            p = (-i + 2 * j, i)
            if p[0] < x_min or p[0] > x_max:
                continue
            if pit(p, p1, p2, p3):
                ans += ncr(i, j)
                ans %= MOD
    print(int(ans))

if DEBUG:
    print(d)
