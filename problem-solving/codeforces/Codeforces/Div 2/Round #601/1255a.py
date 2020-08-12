t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    diff = abs(a - b)
    ans = 0
    if diff == 0:
        print(ans)
    else:
        if diff >= 5:
            ans += diff // 5
            diff %= 5
        if diff >= 2:
            ans += diff // 2
            diff %= 2
        if diff >= 1:
            ans += diff
            diff %= 1
        print(ans)
