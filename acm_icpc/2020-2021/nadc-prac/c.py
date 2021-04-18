x, y = map(int, input().split())
n = int(input())

h = 0
fh = 0

for i in range(n):
    l, u, f = map(float, input().split())
    l = int(l)
    u = int(u)
    if l > y:
        continue
    if u > y:
        h += y - l
        fh += f * (y - l)
    else:
        h += u - l
        fh += f * (u - l)

v = x / (y - h + fh)
print(v)
