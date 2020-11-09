import math


n = int(input())
ans = []
for i in range(n):
    c, s = map(int, input().split())
    if s % c == 0:
        mid = s // c
        ans.append(c * (mid ** 2))
    else:
        low = s // c
        high = math.ceil(s / c)
        ans.append((high ** 2) * (s % c) + (low ** 2) * (c - (s % c)))
print('\n'.join(str(x) for x in ans))
