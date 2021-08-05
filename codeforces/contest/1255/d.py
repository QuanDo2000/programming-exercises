import math


t = int(input())
char = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for _ in range(t):
    r, c, k = map(int, input().split())
    grid = [list(input()) for _ in range(r)]
    ans = [[0 for _ in range(c)] for __ in range(r)]
    rcount = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'R':
                rcount += 1
    uplim = math.ceil(rcount / k)
    lolim = math.floor(rcount / k)
    for i in range(r):
        if (i + 1) % 2 == 0:
            grid[i] = grid[i][::-1]
    # print(*grid)
    if uplim != lolim:
        a = (rcount - k * uplim) / (lolim - uplim)
        b = k - a
    else:
        a = b = rcount // k
    # print(a, b)
    index = 0
    count = 0
    state = 1
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'R':
                count += 1
            if count - 1 == lolim and state:
                if index + 1 == a:
                    state = 0
                index += 1
                count = 1
            elif count - 1 == uplim and not state:
                count = 1
                index += 1
            # print(i, j, count, state, index)
            ans[i][j] = char[index]
    for i in range(r):
        if (i + 1) % 2 == 0:
            ans[i] = ans[i][::-1]
    for i in ans:
        print(''.join(i))
