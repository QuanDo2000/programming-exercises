l, g = map(int, input().split())

# gs = []
hi = -1
for _ in range(g):
    p, d = map(int, input().split())
    # gs.append((p, d))
    if d == 1:
        t = (l - p)
    elif d == 0:
        t = (l - (l - p))
    if t > hi:
        hi = t
print(hi)
