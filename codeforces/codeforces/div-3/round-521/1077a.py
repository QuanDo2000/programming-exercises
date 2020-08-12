t = int(input())
for _ in range(t):
    a, b, k = map(int, input().split())
    ans = (a - b) * (k // 2)
    if k % 2 != 0:
        ans += a
    print(ans)
