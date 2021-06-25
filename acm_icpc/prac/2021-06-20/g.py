import math
t = int(input())
for _ in range(t):
    a, b, m = map(int, input().split())
    n = int(math.sqrt(m)) + 1
    d = {}
    for i in range(n + 1):
        key = pow(a, n * i, m)
        d[key] = i
    for j in range(n):
        key = pow(a, j, m) * b % m
        if key in d:
            i = d[key]
            x = i * n - j
            print(x)
            break
