import math

a, b = map(int, input().split())
res = math.log(b/a, 1.5)
if res == math.ceil(res):
    res += 1
res = math.ceil(res)
print(res)