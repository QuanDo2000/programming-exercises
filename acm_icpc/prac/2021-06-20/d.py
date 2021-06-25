t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    ans = n - p.count(0)
    print(ans)
