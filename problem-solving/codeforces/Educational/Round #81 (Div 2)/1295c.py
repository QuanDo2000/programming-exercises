from bisect import bisect_left


t = int(input())
for _ in range(t):
    s = input()
    t = input()
    d = {}
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = []
        d[s[i]].append(i)

    ans = 1
    j = 0
    for i in range(len(t)):
        if t[i] not in d:
            print(-1)
            break
        nxt = bisect_left(d[t[i]], j)
        if nxt != len(d[t[i]]):
            j = d[t[i]][nxt] + 1
        else:
            j = d[t[i]][0] + 1
            ans += 1
    else:
        print(ans)
