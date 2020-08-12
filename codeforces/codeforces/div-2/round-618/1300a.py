t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = a.count(0)
    if sum(a) + ans == 0:
        ans += 1
    print(ans)
