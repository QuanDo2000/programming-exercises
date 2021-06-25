import sys
import bisect

input = sys.stdin.readline


def lowbit(i):
    return i & (-i)


def update(arr, x, v, uniq_len):
    i = x
    while i <= uniq_len:
        arr[i] += v
        i += lowbit(i)


def query(arr, x):
    result = 0
    i = x
    while i > 0:
        result += arr[i]
        i -= lowbit(i)
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    d = {num: idx for idx, num in enumerate(a)}

    c = [0 for _ in range(n)]
    for idx, num in enumerate(b):
        old_idx = d[num]
        c[old_idx] = idx
    sort_c = sorted(c)
    uniq_len = len(set(c))
    arr = [0 for _ in range(uniq_len + 1)]
    result = 0
    for i in range(n):
        c[i] = bisect.bisect_left(sort_c, c[i]) + 1
    for i in range(n):
        result += query(arr, uniq_len) - query(arr, c[i])
        update(arr, c[i], 1, uniq_len)

    print(result)
