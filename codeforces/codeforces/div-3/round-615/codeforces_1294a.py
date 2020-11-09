t = int(input())
for _ in range(t):
    a, b, c, n = map(int, input().split())
    if (a + b + c + n) % 3 == 0:
        res = (a + b + c + n) // 3
        if res - a >= 0 and res - b >= 0 and res - c >= 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
