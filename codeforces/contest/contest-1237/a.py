import math


state = 0
for _ in range(int(input())):
    a = int(input())
    if a % 2 == 0:
        b = a / 2
    elif state == 0:
        b = math.ceil(a / 2)
        state = 1
    else:
        b = math.floor(a / 2)
        state = 0
    print(int(b))
