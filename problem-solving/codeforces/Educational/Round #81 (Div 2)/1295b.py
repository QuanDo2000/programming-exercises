t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    s = input()
    bal = [0] * (n + 1)
    for i in range(1, n + 1):
        if s[i-1] == '0':
            bal[i] = bal[i-1] + 1
        else:
            bal[i] = bal[i-1] - 1
    mult = bal[-1]
    ans = 0
    if mult == 0:
        if x in bal[1:]:
            print(-1)
        else:
            print(0)
    else:
        for num in bal[1:]:
            if (x - num) % (mult) == 0 and (x - num) / mult >= 0:
                ans += 1
        if x == 0:
            ans += 1
        print(ans)
    # else:
    #     print(0)
    # if x in bal:
    #     if bal.count(x) > 1:
    #         print(-1)
    #     else:
    #         print(1)
    # else:
    #     if bal[-1] < 0:
    #         print(0)
    #     else:
    #         mult = bal[-1]
    #         ans = 0
    #         for num in bal[1:]:
    #             if (x - num) % mult == 0:
    #                 ans += 1
    #         print(ans)
    # print(bal)
