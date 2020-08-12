t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    r = []
    for i in range(n):
        a, b = map(int, input().split())
        l.append(a)
        r.append(b)
    print(max(max(l) - min(r), 0))
