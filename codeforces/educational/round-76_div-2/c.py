t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    temp = {}
    for i in range(n):
        if a[i] not in temp.keys():
            temp[a[i]] = [i]
        else:
            temp[a[i]].append(i)
    ans = 10 ** 9
    for key, val in temp.items():
        if len(val) == 1:
            continue
        else:
            for i in range(1, len(val)):
                if val[i] - val[i-1] + 1 < ans:
                    ans = val[i] - val[i-1] + 1
    if ans == 10 ** 9:
        print(-1)
    else:
        print(ans)
