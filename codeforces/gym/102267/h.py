import math

v, s = map(int, input().split())

r = s / (2 * math.sin(math.radians(180 / v)))
area = math.pi * (r ** 2)
print(area)
