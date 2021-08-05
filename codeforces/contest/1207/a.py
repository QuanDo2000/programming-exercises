t = int(input())
for _ in range(t):
    b, p, f = map(int, input().split())
    h, c = map(int, input().split())
    b = b // 2
    ans = 0
    if h > c:
        s = min(b, p)
        ans += h * s
        b -= s
        p -= s
    else:
        s = min(b, f)
        ans += c * s
        b -= s
        f -= s
    if b and (p or f):
        s = min(b, max(p, f))
        if p:
            ans += h * s
            b -= s
            p -= s
        else:
            ans += c * s
            b -= s
            f -= s
    print(ans)
