import math


t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    if d <= n:
        print('YES')
    else:
        temp = math.ceil(n / 2)
        for x in range(1, temp+1):
            res = x + math.ceil(d / (x + 1))
            if (res) <= n:
                print('YES')
                break
        else:
            print('NO')
