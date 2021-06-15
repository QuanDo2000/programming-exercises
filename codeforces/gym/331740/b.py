t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(lambda x: int(x) % 2, input().split()))
    if 1 not in a:
        print(-1)
    else:
        res = a.count(0)
        print(res)
