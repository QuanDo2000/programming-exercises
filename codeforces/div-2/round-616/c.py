t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    k = min(k, m-1)
    a = list(map(int, input().split()))
    b = []
    for i in range(m):
        b.append(max(a[i], a[i + n - m]))
    sz = m - k
    ans = 0
    j = 0
    q = []
    for i in range(k+1):
        while q and q[0] < i:
            q.pop(0)
        while j < i + sz:
            while q and b[q[-1]] >= b[j]:
                q.pop()
            q.append(j)
            j += 1
        ans = max(ans, b[q[0]])
    print(ans)
