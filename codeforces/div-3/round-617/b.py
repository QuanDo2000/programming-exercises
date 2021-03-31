t = int(input())
for _ in range(t):
    s = int(input())
    ans = s
    while s >= 10:
        inc = s // 10
        ans += inc
        s -= inc * 10
        s += inc
    print(ans)
