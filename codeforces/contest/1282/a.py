t = int(input())
for _ in range(t):
    a, b, c, r = map(int, input().split())
    l, h = c - r, c + r
    if a > b:
        a, b = b, a
    l = max(0, min(h, b) - max(a, l) + 1)
    ans = (b - a + 1) - l
    if l == 0:
        ans -= 1
    # ans = max(l - a, 0) + max(b - h, 0)
    print(ans)
