t = int(input())
ans = []
for _ in range(t):
    n, p, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    # res = 0
    # for i in range(k):
    #     pt = p
    #     if i == k-1:
    #         anst = 0
    #     else:
    #         anst = -k + 1
    #     # print(a[i::k])
    #     for j in a[i::k]:
    #         if pt - j < 0:
    #             break
    #         pt -= j
    #         anst += k
    #     if i != k-1:
    #         for j in a[:i]:
    #             if pt - j < 0:
    #                 break
    #             pt -= j
    #             anst += 1
    #     if res < anst:
    #         res = anst

    pref = 0
    res = 0
    for i in range(k):
        s = pref
        if s > p:
            break
        cnt = i
        for j in range(i+k-1, n, k):
            if s + a[j] <= p:
                cnt += k
                s += a[j]
            else:
                break
        pref += a[i]
        res = max(res, cnt)

    ans.append(res)
print(*ans, sep='\n')
