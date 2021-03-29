import math


t1, t2 = map(int, input().split())
t3 = 80

v1 = t3 - t2
v2 = t1 - t3

num = math.gcd(v1, v2)
v1 /= num
v2 /= num

print(int(v1), int(v2))
