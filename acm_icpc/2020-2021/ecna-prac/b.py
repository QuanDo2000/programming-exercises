import math


def get_price(k):
    global p, a, b, c, d
    return (p * (math.sin(a * k + b) + math.cos(c * k + d) + 2))


p, a, b, c, d, n = map(int, input().split())

prices = [get_price(i) for i in range(1, n + 1)]
mins = [-1] * n

temp = prices[-1]
for i in range(n - 1, -1, -1):
    if temp > prices[i]:
        temp = prices[i]
    mins[i] = temp

ans = None
for i in range(n):
    m = prices[i] - mins[i]
    if ans == None or ans < m:
        ans = m
print(ans)
