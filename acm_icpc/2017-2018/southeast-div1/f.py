import math


EPS = 1e-9
DEBUG = False


def get_intersections(x0, y0, r0, x1, y1, r1):
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1

    d = math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

    # non intersecting
    if d > r0 + r1:
        return None
    # One circle within other
    if d < abs(r0 - r1):
        return None
    # coincident circles
    if d == 0 and r0 == r1:
        return None
    else:
        a = (r0**2 - r1**2 + d**2) / (2 * d)
        h = math.sqrt(r0**2 - a**2)
        x2 = x0 + a * (x1 - x0) / d
        y2 = y0 + a * (y1 - y0) / d
        x3 = x2 + h * (y1 - y0) / d
        y3 = y2 - h * (x1 - x0) / d

        x4 = x2 - h * (y1 - y0) / d
        y4 = y2 + h * (x1 - x0) / d

        return (x3, y3, x4, y4)


def dist(x0, y0, x1, y1):
    return math.hypot(x1 - x0, y1 - y0)


n = int(input())
cs = []

for _ in range(n):
    x, y, d = map(int, input().split())
    cs.append((x, y, d))

points = []
for i in range(n - 1):
    for j in range(i + 1, n):
        c1 = cs[i]
        c2 = cs[j]
        ans = get_intersections(*c1, *c2)
        if ans == None:
            continue
        p1 = round(ans[0], 9), round(ans[1], 9)
        p2 = round(ans[2], 9), round(ans[3], 9)
        if p1 not in points:
            points.append(p1)
        if p2 not in points:
            points.append(p2)
        if DEBUG:
            print(p1, p2, sep='\n')

for i in range(n):
    circle = cs[i]
    r = circle[2]
    v = circle[:2]
    d = dist(0, 0, *v)
    if d != 0:
        p = v[0] + v[0] * r / d, v[1] + v[1] * r / d
    else:
        p = r, 0
    points.append(p)


if DEBUG:
    print(points)

ans = 0.000

for p in points:
    b = True
    for c in cs:
        d = round(dist(*p, *c[:2]), 3)
        if DEBUG:
            print(c, p, d)
        if d > c[2] + EPS:
            b = False
            break
    if DEBUG:
        print(b)
    if b:
        d0 = dist(0, 0, *p)
        if DEBUG:
            print(d0)
        if d0 > ans:
            ans = d0

print('{:.3f}'.format(ans))
