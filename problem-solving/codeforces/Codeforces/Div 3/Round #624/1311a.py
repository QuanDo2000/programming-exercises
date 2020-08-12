t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a == b:
        print(0)
    else:
        diff = b - a
        if diff > 0 and diff % 2 != 0:
            ans = 1
        elif diff > 0 and diff % 2 == 0:
            ans = 2
        elif diff < 0 and diff % 2 == 0:
            ans = 1
        elif diff < 0 and diff % 2 != 0:
            ans = 2
        print(ans)
