import math
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    d = dict()
    x, y = 0, 0
    d[(x, y)] = 0
    l, r = -1, n

    for i in range(n):
        c = s[i]
        if c == 'L':
            x -= 1
        elif c == 'R':
            x += 1
        elif c == 'U':
            y += 1
        elif c == 'D':
            y -= 1

        if (x, y) in d and i - d[(x, y)] < r - l:
            l = d[(x, y)]
            r = i
        d[(x, y)] = i + 1

    if l != -1:
        print(l+1, r+1)
    else:
        print(-1)

    # n = int(input())
    # s = input()
    # ans = ''
    # for i in range(1, n, 2):
    #     if ans == '':
    #         for j in range(n-i):
    #             a = s[j:j+(i+1)]
    #             # print(a)
    #             if a.count('R') == a.count('L') and a.count('U') == a.count('D'):
    #                 ans = '{} {}'.format(j+1, j+(i+1))
    #                 break
    #     else:
    #         break
    # if ans == '':
    #     print(-1)
    # else:
    #     print(ans)
