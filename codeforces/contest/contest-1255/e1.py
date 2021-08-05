# def move(a, x):
#     ri = x + 1
#     li = x - 1
#     l = len(a)
#     while ri < l and a[ri] == 0:
#         ri += 1
#     while li >= 0 and a[li] == 0:
#         li -= 1
#     dr = ri - x
#     dl = x - li
#     if ri == l:
#         return dl, li
#     elif li == -1:
#         return dr, ri
#     if dr < dl:
#         return dr, ri
#     else:
#         return dl, li


# n = int(input())
# a = list(map(int, input().split()))
# ans = 0
# i = 0
# while i < n:
#     if a[i] == 1:
#         d, j = move(a, i)
#         ans += d
#         if j > i:
#             i = j + 1
#             continue
#     i += 1
# if sum(a) == 1:
#     print(-1)
# else:
#     print(ans)


import math


arr = [0] * 1000100
n = 0


# Calculate amount of move for prime number x
def gogo(x):
    global n
    global arr
    cv = 0
    ans = 0
    for i in range(n):
        cv = (cv + arr[i]) % x
        ans += min(cv, x - cv)
        # print(x, i, arr[i], cv, ans)
    return ans


def main():
    global n
    global arr
    n = int(input())
    csum = 0
    arr = list(map(int, input().split()))
    csum = sum(arr)
    # v stores the prime
    v = []
    for i in range(2, math.floor(math.sqrt(csum))):
        if csum % i == 0:
            v.append(i)
            while csum % i == 0:
                csum //= i
    if csum > 1:
        v.append(csum)
    # print(v)
    ans = 3e18
    for f in v:
        # Find minimum amount of moves
        ans = min(ans, gogo(f))
        # print(f, ans)
    if ans > 2e18:
        print(-1)
    else:
        print(ans)


main()
