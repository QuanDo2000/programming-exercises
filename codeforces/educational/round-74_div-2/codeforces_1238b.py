
ans = []
for _ in range(int(input())):
    n, r = map(int, input().split())
    x = set(map(int, input().split()))
    x = sorted(x, reverse=1)
    # print(x, ans)
    # ans = math.ceil(curr / r)
    # last = -1

    # low = 0
    # high = len(x)
    # while low < high:
    #     mid = (high + low) // 2
    #     curr = x[mid]
    #     pos = curr - mid * r
    #     if pos <= 0:
    #         high = mid
    #     else:
    #         low = mid + 1
    # print(low)

    for i, curr in enumerate(x):
        pos = curr - i * r
        if pos <= 0:
            ans.append(i)
            break
    else:
        ans.append(len(x))

print('\n'.join(map(str, ans)))
