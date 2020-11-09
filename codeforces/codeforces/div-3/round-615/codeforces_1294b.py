def main():
    n = int(input())
    p = []
    for i in range(n):
        x, y = map(int, input().split())
        p.append([x, y])
    p.sort()
    max_y = p[0][1]
    for i in range(n):
        if p[i][1] < max_y:
            print('NO')
            return
        else:
            max_y = p[i][1]
    print('YES')
    res = ''
    prev_x = 0
    prev_y = 0
    for i in range(n):
        res += 'R' * (p[i][0] - prev_x)
        res += 'U' * (p[i][1] - prev_y)
        prev_x = p[i][0]
        prev_y = p[i][1]
    print(res)


t = int(input())
for _ in range(t):
    main()
