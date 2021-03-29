from collections import defaultdict


DEBUG = False


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return -1

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    if x < max(min(line1[0][0], line1[1][0]), min(line2[0][0], line2[1][0])) or x > min(max(line1[0][0], line1[1][0]), max(line2[0][0], line2[1][0])) or y < max(min(line1[0][1], line1[1][1]), min(line2[0][1], line2[1][1])) or y > min(max(line1[0][1], line1[1][1]), max(line2[0][1], line2[1][1])):
        return -1
    return int(x), int(y)


def rotate(x, y):
    if (x, y) == (1, 0):
        return (0, 1)
    elif (x, y) == (0, 1):
        return (-1, 0)
    elif (x, y) == (-1, 0):
        return (0, -1)
    else:
        return (1, 0)


def turn(x, y):
    return x * -1, y * -1


def loop(t):
    global state, points, start
    curr = state[0]
    while t > curr:
        if DEBUG:
            print(state)
        nxt = None
        curr = state[0]
        p = state[1][0]
        line = state[2]
        d = state[3]
        for point in points[line]:
            coord = point[0]
            if coord[0] == p[0] and coord[1] != p[1]:
                l = coord[1] - p[1]
                if l * d[1] > 0 and (nxt == None or nxt[1] > abs(l)):
                    nxt = (point, abs(l))
            elif coord[1] == p[1] and coord[0] != p[0]:
                l = coord[0] - p[0]
                if l * d[0] > 0 and (nxt == None or nxt[1] > abs(l)):
                    nxt = (point, abs(l))
        if nxt == None:
            nxt = (state[1], 0)
        if nxt[0][1][0] != nxt[0][1][1]:
            if line == nxt[0][1][0]:
                nxt_line = nxt[0][1][1]
            else:
                nxt_line = nxt[0][1][0]
            nxt_d = (rotate(*d))
        else:
            nxt_line = line
            nxt_d = (turn(*d))
        if curr + nxt[1] > t:
            return state
        state = (curr + nxt[1], nxt[0], nxt_line, nxt_d)
        if state[1][0] == start[0]:
            return state
    return state


n, t = map(int, input().split())
if DEBUG:
    print(n, t)

points = defaultdict(list)
lines = []
for i in range(n):
    bx, by, ex, ey = map(int, input().split())
    if i == 0:
        start = ((bx, by), (i, i))
        if bx == ex:
            if by < ey:
                d = (0, 1)
            else:
                d = (0, -1)
        else:
            if bx < ex:
                d = (1, 0)
            else:
                d = (-1, 0)
    lines.append(((bx, by), (ex, ey)))
    points[i].append(((bx, by), (i, i)))
    points[i].append(((ex, ey), (i, i)))


state = [0, start, 0, d]

if DEBUG:
    print(start)
    print(lines)

for i in range(n - 1):
    for j in range(i + 1, n):
        ans = line_intersection(lines[i], lines[j])
        if type(ans) != int:
            points[i].append((ans, (i, j)))
            points[j].append((ans, (i, j)))
if DEBUG:
    print(points)

tt = loop(t)
if tt[1][0] == start[0] and tt[0] < t:
    state = [0, start, 0, d]
    state = loop(t % tt[0])
    l = (t % tt[0]) - state[0]
else:
    state = tt
    l = t - state[0]

if DEBUG:
    print(t, tt)


p = state[1][0]
d = state[3]
x = p[0] + l * d[0]
y = p[1] + l * d[1]
print(x, y)
