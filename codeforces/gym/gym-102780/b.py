
def check(x):
    global k, r
    total = 0
    for i in range(1, k + 1):
        total += 1 / (1 / rs[i - 1] + 1 / x)
    return total < r + EPS


EPS = 1e-9

k, r = map(int, input().split())

rs = list(map(int, input().split()))


lo = EPS
hi = 10e9

while hi - lo > EPS:
    mid = (lo + hi) / 2
    if check(mid):
        lo = mid
    else:
        hi = mid
print('{:.6f}'.format(mid))
