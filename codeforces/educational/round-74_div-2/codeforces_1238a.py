for _ in range(int(input())):
    x, y = map(int, input().split())
    diff = x - y
    if diff >= 2:
        print('YES')
    else:
        print('NO')