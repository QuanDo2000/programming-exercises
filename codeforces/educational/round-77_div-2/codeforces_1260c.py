import math


t = int(input())
ans = []
for _ in range(t):
    r, b, k = map(int, input().split())
    gcd = math.gcd(r, b)
    if r > b:
        r, b = b, r
    r /= gcd
    b /= gcd
    # Recheck formula
    if ((k - 1) * r + 1) < b:
        ans.append('REBEL')
    else:
        ans.append('OBEY')
print('\n'.join(ans))
