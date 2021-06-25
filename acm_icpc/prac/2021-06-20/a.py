import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    d = {}
    for num in a:
        if num not in d:
            d[num] = 1
        else:
            d[num] += 1
    for __ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            p = query[1] - 1
            v = query[2]
            old = a[p]
            a[p] = v
            d[old] -= 1
            if d[old] <= 0:
                del d[old]
            if v not in d:
                d[v] = 1
            else:
                d[v] += 1
        else:
            ans = len(d)
            if 0 in d:
                print(ans - 1)
            else:
                print(ans)
