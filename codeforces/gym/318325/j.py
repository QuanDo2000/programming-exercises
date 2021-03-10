import math


# def gcd(a, b):
#     while (b):
#         a, b = b, a % b
#     return a


t = int(input())

for _ in range(t):
    c, f, b, s = map(int, input().split())
    hi = math.ceil(s / c) * 360
    mid = s / c * 360
    lo = math.floor(s / c) * 360
    comm = math.gcd(f, b)
    # print(hi, lo, mid, comm)
    for i in range(comm):
        angle = lo + 360 / comm * i
        if angle >= mid and angle % 30 == 0:
            break
    print(int(angle // 30))
