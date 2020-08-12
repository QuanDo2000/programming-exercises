t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [(i+1, c) for i, c in enumerate(map(int, input().split()))]
    a = sorted(a, key=lambda x: x[1])
    # minc = a[0][1] + a[1][1]
    # mine = str(a[0][0]) + ' ' + str(a[1][0])
    sumc = 0
    for i in range(n):
        sumc += a[i][1]
    # print(a)
    # print(minc)
    # print(mine)
    if m < n or n == 2:
        print(-1)
    else:
        ans = 2 * sumc  # + minc * (m - n)
        print(ans)
        for i in range(1, n):
            print(i, i+1)
        print(n, 1)
        # for i in range(m - n):
        #     print(mine)
