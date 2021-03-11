def gcd_ex(a, b):
    aa = (1, 0)
    bb = (0, 1)
    while b != 0:
        if a < b:
            a, b = b, a
            aa, bb = bb, aa
        a -= b
        aa = (aa[0] - bb[0], aa[1] - bb[1])
    return a, aa


def check_axby(x0, y0, a, b):
    if x0 < y0:
        x0, y0 = y0, x0
        a, b = b, a
    t = x0 // b
    if (y0 + t * a) >= 0 and (x0 - t * b) >= 0:
        return True
    return False


def get_sum(pre, x, xx):
    if x == xx:
        return 0
    elif x < xx:
        ans = pre[xx - 1]
        if x - 1 != -1:
            ans -= pre[x - 1]
    else:
        ans = pre[-1] - pre[x - 1]
        if xx - 1 != -1:
            ans += pre[xx - 1]
    return ans


def rec(x, y, z):
    global a, b, c, pre_a, pre_b, r, s, n, pt, dp
    if z == n:
        dp[x][y][z] = 1
        return True
    ret = False
    for i in range(r):
        for j in range(s):
            rem = c[z] - get_sum(pre_a, x, i) - get_sum(pre_b, y, j)
            if DEBUG:
                print(x, y, z, i, j, rem, pt[rem])
            if pt[rem] == 1 and rem >= 0:
                if dp[i][j][z + 1] == 1:
                    return True
                elif dp[i][j][z + 1] == 0:
                    return False
                ret = rec(i, j, z + 1)
            if ret:
                dp[x][y][z] = 1
                return True
    dp[x][y][z] = 0
    return ret


DEBUG = False


r, s, n = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

pt = [0] * (2000000 + 1)

asum = sum(a)
bsum = sum(b)

gcd_ab, pair_ab = gcd_ex(asum, bsum)

for i in range(0, len(pt)):
    if i % gcd_ab == 0:
        x0, y0 = i * pair_ab[0], i * pair_ab[1]
        if check_axby(x0, y0, asum, bsum):
            pt[i] = 1


pre_a = [a[0]] * r
pre_b = [b[0]] * s
for i in range(1, r):
    pre_a[i] = pre_a[i - 1] + a[i]
for i in range(1, s):
    pre_b[i] = pre_b[i - 1] + b[i]


dp = [[[-1 for _ in range(n + 1)] for _ in range(s)] for _ in range(r)]

res = rec(0, 0, 0)
if res:
    print('Yes')
else:
    print('No')


if DEBUG:
    print(asum, bsum)
    print(a, b)
    print(pre_a, pre_b)
    print(gcd_ab, pair_ab)
    # print([i for i in range(len(pt)) if pt[i] == 1])