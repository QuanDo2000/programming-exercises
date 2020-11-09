import math


t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    if x in a:
        print(1)
    else:
        d = max(a)
        print(max(2, math.ceil(x / d)))
