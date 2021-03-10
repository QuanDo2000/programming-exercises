n, k = map(int, input().split())

data = [-1] * k
data[0] = 1
data[-1] = 0
for _ in range(n):
    f, s = input().split()
    if s == 'SAFE':
        b = 1
    else:
        b = 0
    data[int(f) - 1] = b

lo = k - data[::-1].index(1) + 1
hi = data.index(0)

print(lo, hi)
