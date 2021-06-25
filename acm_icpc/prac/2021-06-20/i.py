import math
import sys

input = sys.stdin.readline
pi = math.pi

t = int(input())
for _ in range(t):
    a, b, d = map(int, input().split())
    R = d / 2
    r = math.sqrt(2 * (R ** 2)) / 2
    square = (r * 2) ** 2
    bigC = pi * (R ** 2)
    arc = (bigC - square) / 4
    smallC = pi * (r ** 2)
    ans = (smallC / 2 - arc) * 4
    print(ans)
