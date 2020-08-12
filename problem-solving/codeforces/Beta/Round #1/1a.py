import math


n, m, a = map(int, input().split())
h = math.ceil(n / a)
w = math.ceil(m / a)
ans = h * w
print(ans)
