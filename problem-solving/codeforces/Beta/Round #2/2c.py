import math


# Return point inside line segment that satisfy
# d(p1) / d(p2) = a / b
# d(p1) is distance from point to p1
def iline(p1, p2, a, b):
    x1, y1 = p1
    x2, y2 = p2
    x = (b * x1 + a * x2) / (a + b)
    y = (b * y1 + a * y2) / (a + b)
    return x, y


# Return point outside of line segment that satisfy
# d(p1) / d(p2) = a / b
# d(p1) is distance from point to p1
def oline(p1, p2, a, b):
    x1, y1 = p1
    x2, y2 = p2
    x = (b * x1 - a * x2) / (b - a)
    y = (b * y1 - a * y2) / (b - a)
    return x, y


# Return midpoint of 2 points
def midp(p1, p2):
    return iline(p1, p2, 1, 1)


# Return distance between 2 points
def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


# Determine the center and radius of the circle that contains
# points that have a constant ratio of distance to 2 points.
# Name: Apollonius circle
def locus(c1, c2):
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    ip = iline((x1, y1), (x2, y2), r1, r2)
    op = oline((x1, y1), (x2, y2), r1, r2)
    # print(op)
    mp = midp(ip, op)
    r = dist(mp, ip)
    return mp[0], mp[1], r


# From 2 points, return the perpendicular bisector of the line.
# Return values a, b ,c for the line formula ax + by + c = 0
def line(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    a = x1 - x2
    b = y1 - y2
    c = -(y1**2 - y2**2 + x1**2 - x2**2) / 2
    return a, b, c


# Determine the intersection of 2 circles
def cvc(c1, c2):
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    d = dist((x1, y1), (x2, y2))
    if d > r1 + r2:
        return 0
    elif d == 0 and r1 == r2:
        return -1
    elif d < abs(r1 - r2):
        return []
    elif d == r1 + r2:
        a = (r1**2 - r2**2 + d**2) / (2 * d)
        p2x = x1 + a * (x2 - x1) / d
        p2y = y1 + a * (y2 - y1) / d
        return [(p2x, p2y)]
    else:
        a = (r1**2 - r2**2 + d**2) / (2 * d)
        h = math.sqrt(r1**2 - a**2)
        p2x = x1 + a * (x2 - x1) / d
        p2y = y1 + a * (y2 - y1) / d
        # print(p2x, p2y)
        x31 = p2x + h * (y2 - y1) / d
        y31 = p2y - h * (x2 - x1) / d
        x32 = p2x - h * (y2 - y1) / d
        y32 = p2y + h * (x2 - x1) / d
        # print((x31, y31), (x32, y32))
        return [(x31, y31), (x32, y32)]


# Translate a line of format ax + by + c = 0
# through x, y translation
def linetr(a, b, c, x, y):
    c = c - a * x - b * y
    return a, b, c


# Translate point (a, b) with translation (x, y)
def pointtr(a, b, x, y):
    return a + x, b + y


# Intersection of circle and line
def cvl(c, l):
    la, lb, lc = l
    x1, y1, r1 = c
    la, lb, lc = linetr(la, lb, lc, -x1, -y1)
    d0 = abs(lc) / (math.sqrt(la ** 2 + lb ** 2))
    x = -(la * lc) / (la**2 + lb**2)
    y = -(lb * lc) / (la**2 + lb**2)
    if d0 > r1:
        return []
    elif d0 == r1:
        x, y = pointtr(x, y, x1, y1)
        return [(x, y)]
    else:
        d = r1**2 - (lc**2 / (la**2 + lb**2))
        m = math.sqrt(d / (la**2 + lb**2))
        ax = x + lb * m
        ay = y - la * m
        bx = x - lb * m
        by = y + la * m
        ax, ay = pointtr(ax, ay, x1, y1)
        bx, by = pointtr(bx, by, x1, y1)
        return [(ax, ay), (bx, by)]


# Line vs line intersection
def lvl(l1, l2):
    a1, b1, c1 = l1
    a2, b2, c2 = l2
    if b1 != 0 and b2 != 0:
        if a1 / b1 == a2 / b2:
            if c1 / b1 == c2 / b2:
                return -1
            else:
                return []
        else:
            x = (c1 * b2 - b1 * c2) / (b1 * a2 - a1 * b2)
            y = (c2 * a1 - c1 * a2) / (b1 * a2 - a1 * b2)
            return [(x, y)]
    else:
        x = (c1 * b2 - b1 * c2) / (b1 * a2 - a1 * b2)
        y = (c2 * a1 - c1 * a2) / (b1 * a2 - a1 * b2)
        return [(x, y)]


def main():
    c1 = tuple(map(int, input().split()))
    c2 = tuple(map(int, input().split()))
    c3 = tuple(map(int, input().split()))
    line1, line2, circ1, circ2 = False, False, False, False
    if c1[2] == c2[2]:
        line1 = line(c1[:2], c2[:2])
    else:
        circ1 = locus(c1, c2)
    if c2[2] == c3[2]:
        line2 = line(c2[:2], c3[:2])
    else:
        circ2 = locus(c2, c3)
    if c1[2] == c3[2]:
        line3 = line(c1[:2], c3[:2])
    else:
        circ3 = locus(c1, c3)
    if circ1 and circ2:
        ans = cvc(circ1, circ2)
    elif circ1 and line2:
        ans = cvl(circ1, line2)
    elif circ2 and line1:
        ans = cvl(circ2, line1)
    elif line1 and line2:
        ans = lvl(line1, line2)
    temp = []
    if not ans:
        return
    else:
        for x, y in ans:
            angle = 2 * math.asin(c1[2] / dist((x, y), (c1[0], c1[1])))
            temp.append((x, y, angle))
        ans = sorted(temp, key=lambda x: x[2], reverse=True)
        # print(ans)
        print('{:.6f} {:.6f}'.format(ans[0][0], ans[0][1]))
        return


main()
