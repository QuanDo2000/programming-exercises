import math


def check(l):
    global a
    global b
    global p
    global x
    global y
    global k
    s = [0] * l
    rec = 0
    for i in range(l):
        index = i + 1
        if (index % a == 0):
            s[i] += x
        if (index % b == 0):
            s[i] += y
    s = sorted(s)[::-1]
    for i in range(l):
        rec += p[i] / 100 * s[i]
    return rec >= k


for q in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    x, a = map(int, input().split())
    y, b = map(int, input().split())
    k = int(input())
    p = sorted(p)[::-1]

    low = 0
    high = n + 1
    while low < high:
        mid = (low + high) // 2
        if check(mid):
            high = mid
        else:
            low = mid + 1
    if low > n:
        print(-1)
    else:
        print(low)

    # maxp = max(p)
    # minp = min(p)
    # maxans = maxp * (n // a) * (x / 100) + maxp * (n // b) * (y / 100)
    # minans = minp * (n // a) * (x / 100) + minp * (n // b) * (y / 100)
    # # print(p, maxans, minans)
    # if maxans < k:
    #     print(-1)
    #     return

    # ans = []
    # c = 0
    # for i in range(n):
    #     index = i + 1
    #     if index % a == 0 or index % b == 0:
    #         val = p.pop()
    #         ans.append(val)
    #         if index % a == 0 and index % b == 0:
    #             c += val * ((x + y) / 100)
    #         else:
    #             if index % b == 0:
    #                 c += val * (y / 100)
    #             else:
    #                 c += val * (x / 100)
    #     else:
    #         val = p.pop(0)
    #         ans.append(val)
    #     if c >= k:
    #         break
    # # print(ans, c)
    # lcm = int((a * b) / math.gcd(a, b))
    # if len(ans) >= lcm and lcm != 1:
    #     for i in range(lcm-1, len(ans), lcm):
    #         start = max(i-lcm, 0)
    #         end = min(i, len(ans))
    #         index = ans.index(max(ans[:lcm-1]), 0, lcm-1)
    #         ans[index], ans[i] = ans[i], ans[index]
    #     c = 0
    #     for i in range(len(ans)):
    #         val = ans[i]
    #         index = i + 1
    #         if index % a == 0 and index % b == 0:
    #             c += val * ((x + y) / 100)
    #         else:
    #             if index % b == 0:
    #                 c += val * (y / 100)
    #             if index % a == 0:
    #                 c += val * (x / 100)
    #         if c >= k:
    #             ans = ans[:i+1]
    #             break
    # # print(ans, c)
    # print(len(ans))
