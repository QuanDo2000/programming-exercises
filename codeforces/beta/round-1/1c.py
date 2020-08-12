import math


pi = math.pi
eps = 1e-4


def find_r(x0, y0, x1, y1, x2, y2):
    x01 = x0 - x1
    x02 = x0 - x2

    y01 = y0 - y1
    y02 = y0 - y2

    y20 = y2 - y0
    y10 = y1 - y0

    x20 = x2 - x0
    x10 = x1 - x0

    sx02 = x0 ** 2 - x2 ** 2
    sy02 = y0 ** 2 - y2 ** 2
    sx10 = x1 ** 2 - x0 ** 2
    sy10 = y1 ** 2 - y0 ** 2

    f = ((sx02 * x01) + (sy02 * x01) + (sx10 * x02) +
         (sy10 * x02)) / (2 * ((y20 * x01) - (y10 * x02)))

    g = ((sx02 * y01) + (sy02 * y01) + (sx10 * y02) +
         (sy10 * y02)) / (2 * ((x20 * y01) - (x10 * y02)))

    c = (-(x0 ** 2) - (y0 ** 2) - 2 * g * x0 - 2 * f * y0)

    h = -g
    k = -f
    r = math.sqrt(h ** 2 + k ** 2 - c)
    return r


def distance(x0, y0, x1, y1):
    return math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)


def law_of_cos(a, b, c):
    angle = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
    return angle


def all_angles(x0, y0, x1, y1, x2, y2):
    d01 = distance(x0, y0, x1, y1)
    d12 = distance(x1, y1, x2, y2)
    d02 = distance(x0, y0, x2, y2)
    a0 = law_of_cos(d01, d02, d12)
    a1 = law_of_cos(d01, d12, d02)
    a2 = law_of_cos(d12, d02, d01)
    return a0, a1, a2


def gcd(x, y):
    while (abs(x) > eps and abs(y) > eps):
        if (x > y):
            x -= math.floor(x / y) * y
        else:
            y -= math.floor(y / x) * x
    return x + y


x0, y0 = map(float, input().split())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
r = find_r(x0, y0, x1, y1, x2, y2)
a0, a1, a2 = all_angles(x0, y0, x1, y1, x2, y2)
n = pi / gcd(gcd(a0, a1), a2)
a = 0.5 * n * (r ** 2) * math.sin((2 * pi) / n)
print('{:f}'.format(a))
