for q in range(int(input())):
    h, n = map(int, input().split())
    p = list(map(int, input().split()))
    # s = [0] * h
    # for plat in p:
    #     s[h-plat] = 1
    p.append(0)
    ans = 0
    i = 1
    # print(s)
    while i < n:
        if p[i] - 1 == p[i+1]:
            i += 2
        else:
            ans += 1
            i += 1
    print(ans)
