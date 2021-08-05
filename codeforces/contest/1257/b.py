t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if x >= y:
        print('YES')
    elif x == 1:
        if y != 1:
            print('NO')
        else:
            print('YES')
    elif x <= 3:
        if y <= 3:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')
